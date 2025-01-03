from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiUrlEndsWithSlashError(Exception):
    pass


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    api_url: str
    oauth_endpoint: str
    oauth_client_id: str
    oauth_client_secret: str
    oauth_realm_id: str
    file_sink_path: str

    @field_validator("api_url", "oauth_endpoint")
    def validate_api_url(cls, api_url: str):
        if not api_url.strip().endswith("/"):
            return api_url
        else:
            raise ApiUrlEndsWithSlashError(f"API URL {api_url} must not end with a slash")
