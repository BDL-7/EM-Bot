import test from "node:test";
import assert from "node:assert/strict";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const { start } = require("../host_app/static/auth-check.js");

function setup(fetch) {
  let click;
  const button = { disabled: false, addEventListener: (_, fn) => { click = fn; } };
  const status = { textContent: "" };
  const elements = {
    "test-token-connection": button,
    "token-test-status": status,
    "microbot-config": { textContent: JSON.stringify({ tokenEndpoint: "/content/example/api/edav-token" }) },
  };
  start({ getElementById: id => elements[id] }, { fetch });
  return { button, status, click };
}

test("success does not read or display the token response", async () => {
  const state = setup(async (url, options) => {
    assert.equal(url, "/content/example/api/edav-token");
    assert.equal(options.method, "POST");
    assert.equal(options.credentials, "same-origin");
    return { status: 200, json: () => { throw Error("Token body must not be read"); } };
  });
  await state.click();
  assert.match(state.status.textContent, /HTTP 200/);
  assert.equal(state.button.disabled, false);
});

test("failure displays a valid reference but no raw provider fields", async () => {
  const reference = "12345678-1234-4234-8234-123456789abc";
  const state = setup(async () => ({
    status: 502, json: async () => ({ diagnostic_id: reference, message: "secret", token: "bearer" }),
  }));
  await state.click();
  assert.ok(state.status.textContent.includes(reference));
  assert.ok(!state.status.textContent.includes("secret"));
  assert.ok(!state.status.textContent.includes("bearer"));
});

test("proxy HTML, invalid references, and network errors recover without disclosure", async () => {
  for (const fetch of [
    async () => ({ status: 502, json: async () => { throw Error("sensitive proxy body"); } }),
    async () => ({ status: 502, json: async () => ({ diagnostic_id: "secret" }) }),
    async () => { throw Error("secret"); },
  ]) {
    const state = setup(fetch);
    await state.click();
    assert.equal(state.button.disabled, false);
    assert.ok(!state.status.textContent.includes("secret"));
    assert.ok(!state.status.textContent.includes("sensitive"));
  }
});
