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

  function buildIntegrationUrl(baseUrl, integrationId) {
    const url = new URL(baseUrl);
    url.searchParams.set("IntegrationId", integrationId);
    url.searchParams.set("ShowHeader", "false");
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
    const openButton = doc.getElementById("open-microbot");

    let iframe = null;
    let nonce = null;
    let stopResending = null;
    let generation = 0;

    function cancelResending() {
      if (stopResending) stopResending();
      stopResending = null;
    }

    function setStatus(message, ready) {
      status.textContent = message;
      status.className = "chat-status " + (ready ? "good" : "pending");
    }

    function cleanup() {
      generation += 1;
      win.removeEventListener("message", onMessage);
      cancelResending();
      if (iframe) iframe.remove();
      iframe = null;
      nonce = null;
      panel.hidden = true;
      closeButton.hidden = true;
      openButton.hidden = false;
      setStatus("Chat closed. Reopen it to reload the chat.", false);
      openButton.focus();
    }

    function onMessage(event) {
      if (!iframe || event.origin !== config.origin || event.source !== iframe.contentWindow) return;
      if (config.requiresToken !== false && nonce && isAcknowledgment(event, config.origin, nonce)) {
        cancelResending();
        setStatus("Token acknowledged; verify the chat response.", true);
        return;
      }
      if (event.data && event.data.type === "EVA_CLOSE_REQUESTED") cleanup();
    }

    function isCurrent(targetFrame, session) {
      return iframe === targetFrame && generation === session;
    }

    async function authenticateFrame(targetFrame, session) {
      const response = await win.fetch(config.tokenEndpoint, {
        method: "POST",
        credentials: "same-origin",
        headers: { Accept: "application/json" },
      });
      if (!isCurrent(targetFrame, session)) return;
      const payload = await response.json();
      if (!isCurrent(targetFrame, session)) return;
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
      stopResending = repeatUntilStopped(
        function (attempt) {
          if (!isCurrent(targetFrame, session) || !targetFrame.contentWindow) return;
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
            if (!isCurrent(targetFrame, session)) return;
            stopResending = null;
            setStatus(
              "No acknowledgment from Microbot after " + MAX_TOKEN_SEND_ATTEMPTS +
                " attempts. See Technical details for connection testing.",
              false
            );
          },
        }
      );
    }

    if (!config.ready) {
      setStatus("Chat is not configured. See Technical details for what is needed.", false);
      return { cleanup: cleanup };
    }

    function open() {
      if (iframe) return;
      const session = ++generation;
      const targetFrame = doc.createElement("iframe");
      iframe = targetFrame;
      const requiresToken = config.requiresToken !== false;
      targetFrame.title = "EM Knowledge Assistant";
      if (requiresToken) {
        targetFrame.src = buildIframeUrl(config.baseUrl, config.clientId, Date.now());
      } else {
        targetFrame.src = buildIntegrationUrl(config.baseUrl, config.integrationId);
        targetFrame.allow = "clipboard-write";
        targetFrame.loading = "lazy";
        targetFrame.className = "integration-iframe";
      }
      targetFrame.addEventListener("load", function () {
        if (!isCurrent(targetFrame, session)) return;
        if (!requiresToken) {
          setStatus("Iframe loaded; verify chat response", false);
          return;
        }
        authenticateFrame(targetFrame, session).catch(function (error) {
          if (isCurrent(targetFrame, session)) {
            setStatus(error.message + ". See Technical details for connection testing.", false);
          }
        });
      });
      win.addEventListener("message", onMessage);
      container.appendChild(targetFrame);
      panel.hidden = false;
      closeButton.hidden = false;
      openButton.hidden = true;
      setStatus("Loading Microbot", false);
    }

    closeButton.addEventListener("click", cleanup);
    openButton.addEventListener("click", function () {
      open();
      closeButton.focus();
    });
    open();
    return { cleanup: cleanup };
  }

  return {
    buildIframeUrl: buildIframeUrl,
    buildIntegrationUrl: buildIntegrationUrl,
    isAcknowledgment: isAcknowledgment,
    isValidJwt: isValidJwt,
    repeatUntilStopped: repeatUntilStopped,
    start: start,
  };
});
