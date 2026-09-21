(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  } else {
    root.EmMicrobot = api;
    document.addEventListener("DOMContentLoaded", () => api.start(document, window));
  }
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";

  function isValidJwt(token) {
    return typeof token === "string" && token.split(".").length === 3;
  }

  function buildIframeUrl(baseUrl, clientId, timestamp) {
    const url = new URL(baseUrl);
    url.searchParams.set("clientId", clientId);
    url.searchParams.set("_t", String(timestamp));
    return url.toString();
  }

  function isAcknowledgment(event, expectedOrigin, expectedNonce) {
    return (
      event.origin === expectedOrigin &&
      event.data &&
      event.data.type === "TOKEN_ACKNOWLEDGED" &&
      event.data.nonce === expectedNonce
    );
  }

  function start(doc, win) {
    const configElement = doc.getElementById("microbot-config");
    if (!configElement) return { cleanup: function () {} };
    const config = JSON.parse(configElement.textContent);
    const status = doc.getElementById("iframe-status");
    const panel = doc.getElementById("microbot-panel");
    const container = doc.getElementById("microbot-container");
    const closeButton = doc.getElementById("close-microbot");

    let iframe = null;
    let nonce = null;

    function setStatus(message, ready) {
      status.textContent = message;
      status.className = ready ? "good" : "pending";
    }

    function cleanup() {
      win.removeEventListener("message", onMessage);
      if (iframe) iframe.remove();
      iframe = null;
      nonce = null;
      panel.hidden = true;
      setStatus("Closed", false);
    }

    function onMessage(event) {
      if (event.origin !== config.origin) return;
      if (isAcknowledgment(event, config.origin, nonce)) {
        setStatus("Token acknowledged; Microbot ready", true);
        return;
      }
      if (event.data && event.data.type === "EVA_CLOSE_REQUESTED") cleanup();
    }

    async function authenticateFrame() {
      const response = await win.fetch(config.tokenEndpoint, {
        method: "POST",
        credentials: "same-origin",
        headers: { Accept: "application/json" },
      });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.message || "EDAV token request failed");
      if (!isValidJwt(payload.token)) throw new Error("EDAV token response was not a JWT");
      nonce = win.crypto.randomUUID();
      iframe.contentWindow.postMessage(
        {
          type: "EDAV_AUTH_TOKEN",
          payload: {
            token: payload.token,
            expiresAt: payload.expiresAt,
            nonce: nonce,
            userProfile: payload.userProfile || undefined,
          },
        },
        config.origin
      );
      setStatus("Token sent; waiting for acknowledgment", false);
    }

    if (!config.ready) {
      setStatus("Blocked by pending EDAV configuration", false);
      return { cleanup: cleanup };
    }

    iframe = doc.createElement("iframe");
    iframe.title = "EM Knowledge Bot";
    iframe.src = buildIframeUrl(config.baseUrl, config.clientId, Date.now());
    iframe.addEventListener("load", function () {
      authenticateFrame().catch(function (error) {
        setStatus(error.message, false);
      });
    });
    win.addEventListener("message", onMessage);
    closeButton.addEventListener("click", cleanup, { once: true });
    container.appendChild(iframe);
    panel.hidden = false;
    setStatus("Iframe loaded; authentication pending", false);
    return { cleanup: cleanup };
  }

  return {
    buildIframeUrl: buildIframeUrl,
    isAcknowledgment: isAcknowledgment,
    isValidJwt: isValidJwt,
    start: start,
  };
});
