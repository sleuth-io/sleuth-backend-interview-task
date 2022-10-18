import os

from flask import Flask, Response, request
from flask import jsonify

import logging

from github import GithubREST

dev_mode = True
app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(message)s",
)


@app.route("/")
def health_check() -> dict:
    return {
        "data": "Hello, welcome to Sleuth backend interview task. Please see instructions in README.md"
    }


@app.route("/health/github")
def github_api_root_example() -> dict:
    return GithubREST().get("/")


@app.route("/github/repos/<path:repository>/pulls", methods=["GET"])
def github_repository_pull_requests(repository: str):
    # list repos PRs: https://docs.github.com/en/rest/pulls/pulls#list-pull-requests
    # example of a repository with lots of PRs: https://github.com/django/django

    return {"data": f"TODO: got {repository=}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
