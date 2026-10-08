(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    document.addEventListener("DOMContentLoaded", () => api.start(document, window));
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  function start(doc, win) {
    const button = doc.getElementById("test-token-connection");
    const status = doc.getElementById("token-test-status");
    const configElement = doc.getElementById("microbot-config");
    if (!button || !status || !configElement) return;
    const config = JSON.parse(configElement.textContent);
    button.addEventListener("click", async function () {
      button.disabled = true;
      status.textContent = "Testing the server connection to Entra...";
      try {
        const response = await win.fetch(config.tokenEndpoint, {
          method: "POST",
          credentials: "same-origin",
          headers: { Accept: "application/json" },
        });
        if (response.status === 200) {
          // Do not parse, display, or log the successful response's token.
          status.textContent = "HTTP 200: token acquisition succeeded. Iframe acceptance is a separate test.";
        } else {
          let reference = "";
          try {
            const payload = await response.json();
            if (typeof payload.diagnostic_id === "string" &&
                /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(payload.diagnostic_id)) {
              reference = " Diagnostic reference: " + payload.diagnostic_id;
            }
          } catch (_) { /* Proxy errors may not have a JSON body. */ }
          status.textContent = "HTTP " + response.status + ": token test failed." + reference +
            " Review the status guide and Connect runtime logs.";
        }
      } catch (_) {
        status.textContent = "The browser could not reach the token endpoint. Check Network and Connect runtime logs.";
      } finally {
        button.disabled = false;
      }
    });
  }
  return { start: start };
});
