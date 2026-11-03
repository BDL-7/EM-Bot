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

  const MAX_TOKEN_SEND_ATTEMPTS = 10;
  const TOKEN_RESEND_INTERVAL_MS = 1000;

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

  // The iframe's load event can fire before the Microbot app registers its message
  // listener, so the same message is resent until it is acknowledged.
  function repeatUntilStopped(send, options) {
    let attempts = 0;
    let timer = null;
    function stop() {
      if (timer !== null) options.clearInterval(timer);
      timer = null;
    }
    function attempt() {
      if (attempts >= options.maxAttempts) {
        stop();
        options.onExhausted();
        return;
      }
      attempts += 1;
      send(attempts);
    }
    attempt();
    timer = options.setInterval(attempt, options.intervalMs);
    return stop;
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
    let stopResending = null;

    function cancelResending() {
      if (stopResending) stopResending();
      stopResending = null;
    }

    function setStatus(message, ready) {
      status.textContent = message;
      status.className = ready ? "good" : "pending";
    }

    function cleanup() {
      win.removeEventListener("message", onMessage);
      cancelResending();
      if (iframe) iframe.remove();
      iframe = null;
      nonce = null;
      panel.hidden = true;
      setStatus("Closed", false);
    }

    function onMessage(event) {
      if (event.origin !== config.origin) return;
      if (isAcknowledgment(event, config.origin, nonce)) {
        cancelResending();
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
      cancelResending();
      nonce = win.crypto.randomUUID();
      const message = {
        type: "EDAV_AUTH_TOKEN",
        payload: {
          token: payload.token,
          expiresAt: payload.expiresAt,
          nonce: nonce,
          userProfile: payload.userProfile || undefined,
        },
      };
      const targetFrame = iframe;
      stopResending = repeatUntilStopped(
        function (attempt) {
          if (!targetFrame.contentWindow) return;
          targetFrame.contentWindow.postMessage(message, config.origin);
          setStatus(
            "Token sent (attempt " + attempt + " of " + MAX_TOKEN_SEND_ATTEMPTS +
              "); waiting for acknowledgment",
            false
          );
        },
        {
          maxAttempts: MAX_TOKEN_SEND_ATTEMPTS,
          intervalMs: TOKEN_RESEND_INTERVAL_MS,
          setInterval: win.setInterval.bind(win),
          clearInterval: win.clearInterval.bind(win),
          onExhausted: function () {
            stopResending = null;
            setStatus(
              "No acknowledgment from Microbot after " + MAX_TOKEN_SEND_ATTEMPTS +
                " attempts; check that this host origin is allowed for the clientId",
              false
            );
          },
        }
      );
    }

    if (!config.ready) {
      setStatus("Blocked by pending EDAV configuration", false);
      return { cleanup: cleanup };
    }

    iframe = doc.createElement("iframe");
    iframe.title = "EM Knowledge Bot";
    iframe.src = buildIframeUrl(config.baseUrl, config.clientId, Date.now());
    const requiresToken = config.requiresToken !== false;
    iframe.addEventListener("load", function () {
      if (!requiresToken) {
        setStatus("Microbot loaded (no token required)", true);
        return;
      }
      authenticateFrame().catch(function (error) {
        setStatus(error.message, false);
      });
    });
    win.addEventListener("message", onMessage);
    closeButton.addEventListener("click", cleanup, { once: true });
    container.appendChild(iframe);
    panel.hidden = false;
    setStatus(
      requiresToken ? "Iframe loaded; authentication pending" : "Loading Microbot",
      false
    );
    return { cleanup: cleanup };
  }

  return {
    buildIframeUrl: buildIframeUrl,
    isAcknowledgment: isAcknowledgment,
    isValidJwt: isValidJwt,
    repeatUntilStopped: repeatUntilStopped,
    start: start,
  };
});
