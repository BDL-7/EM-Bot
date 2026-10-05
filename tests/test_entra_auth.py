import pytest

from host_app.entra_auth import EntraTokenProvider, TokenProviderError


class FakeApplication:
    def __init__(self, response):
        self.response = response
        self.scopes = []

    def acquire_token_for_client(self, *, scopes):
        self.scopes.append(scopes)
        return self.response


def test_provider_uses_expected_authority_scope_and_cache():
    observed = {}
    application = FakeApplication({"access_token": "one.two.three", "expires_in": 3600})

    def factory(**kwargs):
        observed.update(kwargs)
        return application

    provider = EntraTokenProvider(
        tenant_id="tenant-id",
        client_id="client-id",
        client_secret="test-only-secret",
        scope="api://edav-microbot/.default",
        application_factory=factory,
        clock=lambda: 1_000,
    )

    first = provider.get_token()
    second = provider.get_token()

    assert first == second
    assert first.value == "one.two.three"
    assert first.expires_at == 4_600
    assert application.scopes == [["api://edav-microbot/.default"]]
    assert observed == {
        "client_id": "client-id",
        "authority": "https://login.microsoftonline.com/tenant-id",
        "client_credential": "test-only-secret",
    }


@pytest.mark.parametrize(
    "response",
    [
        {"error": "invalid_client", "error_description": "test-only-secret"},
        {"access_token": "one.two.three", "expires_in": 0},
        {"access_token": "one.two.three", "expires_in": "not-a-number"},
    ],
)
def test_provider_sanitizes_failed_or_invalid_token_responses(response):
    provider = EntraTokenProvider(
        tenant_id="tenant-id",
        client_id="client-id",
        client_secret="test-only-secret",
        scope="api://edav-microbot/.default",
        application_factory=lambda **kwargs: FakeApplication(response),
        clock=lambda: 1_000,
    )

    with pytest.raises(TokenProviderError, match="EDAV token acquisition failed") as error:
        provider.get_token()

    assert "test-only-secret" not in str(error.value)
