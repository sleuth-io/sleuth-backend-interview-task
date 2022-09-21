from dataclasses import dataclass
from typing import Any

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10


def to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


@dataclass
class QueryParams:
    page: int  # number of page
    per_page: int  # number of objects per page

    def __post_init__(self):
        self.page = to_int(self.page, DEFAULT_PAGE)
        self.per_page = to_int(self.per_page, DEFAULT_PER_PAGE)
