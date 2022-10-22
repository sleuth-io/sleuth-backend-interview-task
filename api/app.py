import logging

from flask import Flask

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


@app.route("/swapi/<int:min_cargo_capacity>/vehicles", methods=["GET"])
def swapi_min_cargo_capacity_vehicles(min_cargo_capacity: int) -> dict:
    """Lists vehicles with cargo capacity that is greater or equal to the provided value.

    For each vehicle list the attrs: name, model and cargo capacity
    """

    # TODO

    return {
        "available_vehicles": f"TODO, list vehicles with cargo capacity that is greater or equal to the provided value."
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
