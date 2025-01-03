import logging
from typing import List

import requests
from cachetools import func
from tenacity import stop_after_attempt, wait_exponential, before_sleep_log, retry

from import_export.models import ImportEntry


class ApiClient:

    def __init__(self, url: str, oauth_token_endpoint: str, client_id: str, client_secret: str, realm_id: str):
        self.url = url
        self.oauth_token_endpoint = oauth_token_endpoint
        self.client_id = client_id
        self.client_secret = client_secret
        self.realm_id = realm_id

    def get_entries(self) -> List[ImportEntry]:
        access_token = self._get_access_token()
        response = requests.post(
            self.url,
            json={},
            headers={
                "Content-Type": "application/json;charset=utf-8",
                "Authorization": f"Bearer {access_token}",
            },
        )
        response.raise_for_status()
        result = [
            ImportEntry(user_id=entry["id"], first_name=entry["first_name"], last_name=entry["last_name"])
            for entry in response.json()["entries"]
        ]
        return result

    @func.ttl_cache(maxsize=1, ttl=3540)
    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=30),
        before_sleep=before_sleep_log(logging.getLogger(), logging.INFO),
    )
    def _get_access_token(self) -> str:
        response = requests.post(
            self.oauth_token_endpoint,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "realm_id": self.realm_id,
            },
            timeout=10.0,
        )
        response.raise_for_status()
        return response.json()["access_token"]
