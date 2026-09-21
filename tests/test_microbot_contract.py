from pathlib import Path


SCRIPT = (Path(__file__).parents[1] / "host_app" / "static" / "microbot.js").read_text(
    encoding="utf-8"
)


def test_protocol_uses_exact_origin_not_wildcard():
    assert "postMessage(" in SCRIPT
    assert "config.origin" in SCRIPT
    assert 'postMessage(message, "*")' not in SCRIPT
    assert "event.origin !== config.origin" in SCRIPT


def test_protocol_validates_acknowledgment_nonce():
    assert 'event.data.type === "TOKEN_ACKNOWLEDGED"' in SCRIPT
    assert "event.data.nonce === expectedNonce" in SCRIPT


def test_protocol_handles_close_and_listener_cleanup():
    assert 'event.data.type === "EVA_CLOSE_REQUESTED"' in SCRIPT
    assert 'removeEventListener("message", onMessage)' in SCRIPT


def test_protocol_does_not_create_iframe_until_ready():
    readiness_gate = SCRIPT.index("if (!config.ready)")
    iframe_creation = SCRIPT.index('doc.createElement("iframe")')
    assert readiness_gate < iframe_creation
