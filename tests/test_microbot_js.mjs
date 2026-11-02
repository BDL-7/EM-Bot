import assert from "node:assert/strict";
import { createRequire } from "node:module";
import test from "node:test";

const require = createRequire(import.meta.url);
const protocol = require("../host_app/static/microbot.js");

test("validates only three-part JWT-shaped strings", () => {
  assert.equal(protocol.isValidJwt("one.two.three"), true);
  assert.equal(protocol.isValidJwt("one.two"), false);
  assert.equal(protocol.isValidJwt(null), false);
});

test("builds an iframe URL with clientId and cache timestamp", () => {
  const url = new URL(
    protocol.buildIframeUrl("https://microbot.example/", "em-bot", 12345)
  );
  assert.equal(url.origin, "https://microbot.example");
  assert.equal(url.searchParams.get("clientId"), "em-bot");
  assert.equal(url.searchParams.get("_t"), "12345");
});

test("accepts an acknowledgment only from the expected origin and nonce", () => {
  const expected = "https://microbot.example";
  const event = {
    origin: expected,
    data: { type: "TOKEN_ACKNOWLEDGED", nonce: "known-nonce" },
  };
  assert.equal(protocol.isAcknowledgment(event, expected, "known-nonce"), true);
  assert.equal(protocol.isAcknowledgment(event, "https://evil.example", "known-nonce"), false);
  assert.equal(protocol.isAcknowledgment(event, expected, "wrong-nonce"), false);
});

function fakeTimers() {
  const timers = { callback: null, cleared: false };
  timers.setInterval = (callback) => {
    timers.callback = callback;
    return 1;
  };
  timers.clearInterval = () => {
    timers.cleared = true;
  };
  return timers;
}

test("resends until stopped, without exceeding the attempt limit", () => {
  const timers = fakeTimers();
  const sent = [];
  let exhausted = false;
  const stop = protocol.repeatUntilStopped((attempt) => sent.push(attempt), {
    maxAttempts: 3,
    intervalMs: 1000,
    setInterval: timers.setInterval,
    clearInterval: timers.clearInterval,
    onExhausted: () => {
      exhausted = true;
    },
  });
  timers.callback();
  stop();
  assert.deepEqual(sent, [1, 2]);
  assert.equal(timers.cleared, true);
  assert.equal(exhausted, false);
});

test("reports exhaustion when no acknowledgment arrives", () => {
  const timers = fakeTimers();
  const sent = [];
  let exhausted = false;
  protocol.repeatUntilStopped((attempt) => sent.push(attempt), {
    maxAttempts: 2,
    intervalMs: 1000,
    setInterval: timers.setInterval,
    clearInterval: timers.clearInterval,
    onExhausted: () => {
      exhausted = true;
    },
  });
  timers.callback();
  timers.callback();
  assert.deepEqual(sent, [1, 2]);
  assert.equal(exhausted, true);
  assert.equal(timers.cleared, true);
});

function fakePage(config) {
  const elements = {};
  const make = (id) => {
    const el = {
      id,
      hidden: true,
      textContent: "",
      className: "",
      children: [],
      listeners: {},
      appendChild(child) {
        this.children.push(child);
      },
      addEventListener(type, handler) {
        this.listeners[type] = handler;
      },
      remove() {},
    };
    elements[id] = el;
    return el;
  };
  ["iframe-status", "microbot-panel", "microbot-container", "close-microbot"].forEach(make);
  make("microbot-config").textContent = JSON.stringify(config);
  const doc = {
    getElementById: (id) => elements[id] || null,
    createElement: () => make("iframe"),
  };
  const fetchCalls = [];
  const win = {
    fetch: (...args) => {
      fetchCalls.push(args);
      return Promise.reject(new Error("fetch should not be called"));
    },
    addEventListener() {},
    removeEventListener() {},
  };
  return { elements, doc, win, fetchCalls };
}

test("no-token mode loads the Microbot without requesting a token", async () => {
  const page = fakePage({
    baseUrl: "https://microbot.example/",
    origin: "https://microbot.example",
    clientId: "em-bot",
    ready: true,
    requiresToken: false,
    tokenEndpoint: "/api/edav-token",
  });
  protocol.start(page.doc, page.win);
  const iframe = page.elements["iframe"];
  assert.equal(new URL(iframe.src).searchParams.get("clientId"), "em-bot");
  assert.equal(page.elements["microbot-panel"].hidden, false);
  iframe.listeners.load();
  await Promise.resolve();
  assert.equal(page.fetchCalls.length, 0);
  assert.equal(page.elements["iframe-status"].textContent, "Microbot loaded (no token required)");
});
