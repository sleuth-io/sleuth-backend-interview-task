from __future__ import annotations

import logging

import requests

logger = logging.getLogger(__name__)


class SWApi:
    API_URL = "https://swapi.dev/api"

    def get(self, url_path: str, params: dict | None = None) -> requests.Response:
        """Call StarWars API. `url_path` should be with starting /."""
        if url_path and url_path.startswith("https://"):
            full_url = url_path
        else:
            full_url = f"{self.API_URL}{url_path}"

        logger.info(f"SWAPI GET request {full_url=}, {params=}")
        response = requests.get(
            full_url,
            params=params,
        )
        return response
