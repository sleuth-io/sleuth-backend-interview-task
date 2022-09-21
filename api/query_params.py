from dataclasses import dataclass


@dataclass
class QueryParams:
    page: int  # number of page
    per_page: int  # number of objects per page
