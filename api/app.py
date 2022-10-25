import logging

from flask import Flask
from flask import request

from swapi import SWApi

dev_mode = True
app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(asctime)s %(message)s",
)


@app.route("/")
def index() -> dict:
    return {
        "data": "Hello, welcome to Sleuth backend interview task. Please see instructions in README.md"
    }


@app.route("/health")
def health_check() -> dict:
    response = SWApi().get("/")
    return {"swapi_is_healthy": response.status_code == 200, "urls": response.json()}


@app.route("/swapi/vehicles", methods=["GET"])
def swapi_min_cargo_capacity_vehicles() -> dict:
    """Lists vehicles with cargo capacity that is greater or equal to the provided value.

    For each vehicle list the attrs: name, model and cargo capacity
    """
    min_cargo_capacity = request.args.get("min_cargo_capacity")

    # TODO

    return {
        "available_vehicles": f"TODO, list vehicles with cargo capacity that is greater or equal to {min_cargo_capacity=}."
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
