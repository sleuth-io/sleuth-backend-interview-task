import logging
from typing import Optional

import requests

logger = logging.getLogger(__name__)


# https://docs.github.com/en/rest
class GithubREST:
    API_URL = "https://api.github.com"

    def get(self, url_path: str, params: Optional[dict] = None) -> dict:
        """Call GitHub API. `url_path` should be with starting /."""
        if url_path and url_path.startswith("https://"):
            full_url = url_path
        else:
            full_url = f"{self.API_URL}{url_path}"

        logger.info(f"Github GET request {full_url=}, {params=}")
        response = requests.get(
            full_url,
            params=params,
        )
        data = response.json()
        return {"links": response.links, "data": data}
