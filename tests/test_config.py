import pytest
from hamcrest import assert_that, equal_to

from import_export.config import Settings, ApiUrlEndsWithSlashError


class TestSettings:

    def test_load_settings(self):
        # Given
        api_url = "fake_api_url"
        oauth_endpoint = "fake_oauth_endpoint"
        oauth_client_id = "fake_oauth_client_id"
        oauth_client_secret = "fake_oauth_client_secret"
        oauth_realm_id = "fake_oauth_realm_id"
        file_sink_path = "fake_file_sink_path"

        # When
        settings = Settings(
            api_url=api_url,
            oauth_endpoint=oauth_endpoint,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
            oauth_realm_id=oauth_realm_id,
            file_sink_path=file_sink_path,
        )

        # Then
        assert_that(settings.api_url, equal_to(api_url))
        assert_that(settings.oauth_endpoint, equal_to(oauth_endpoint))
        assert_that(settings.oauth_client_id, equal_to(oauth_client_id))
        assert_that(settings.oauth_client_secret, equal_to(oauth_client_secret))
        assert_that(settings.oauth_realm_id, equal_to(oauth_realm_id))
        assert_that(settings.file_sink_path, equal_to(file_sink_path))

    def test_invalid_api_url(self):
        # Given
        fake_api_url = "https://api.example.com/"

        # When & Then
        with pytest.raises(ApiUrlEndsWithSlashError):
            _ = Settings(api_url=fake_api_url)