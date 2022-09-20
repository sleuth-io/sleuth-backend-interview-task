import os

from flask import Flask, Response
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
