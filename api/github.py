import logging
from typing import Optional

import requests

logger = logging.getLogger(__name__)


class GithubREST:
    API_URL = "https://api.github.com"

    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token

    def _request_headers(self):
        return {
            "Accept": "application/vnd.github.moondragon+json",
            "Authorization": f"Bearer {self.api_token}",
        }

    def get(self, url_path: str):
        """Call GitHub API. `url_path` should be with starting /."""
        if url_path and url_path.startswith("https://"):
            full_url = url_path
        else:
            full_url = f"{self.API_URL}{url_path}"

        logger.info(f"Github GET request {full_url=}")
        response = requests.get(
            full_url,
            headers=self._request_headers(),
        )
        data = response.json()
        return data
