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
