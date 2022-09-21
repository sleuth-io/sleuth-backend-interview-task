import os

from flask import Flask, Response, request
from flask import jsonify

import logging

from github import GithubREST
from query_params import QueryParams

dev_mode = True
app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(message)s",
)


@app.route("/health")
def health_check() -> Response:
    return jsonify("OK")


@app.route("/github/whoami")
def github_whoami():
    logger.info("Github whoami called")
    token = os.getenv("GITHUB_API_TOKEN")
    if not token:
        return {"error": "Github token not set"}

    return GithubREST(token).get("/user")


@app.route("/github/pulls/<path:repository>", methods=["GET"])
def github_repository_pull_requests(repository: str):
    # collect query params
    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 10)
    query_params = QueryParams(page=page, per_page=per_page)

    return {"data": "TODO"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
