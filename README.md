# Sleuth backend interview task

Hello, and welcome to backend interview task :wave:

At Sleuth, we integrate with many providers and gather useful information that help our customers track engineering efficiency.
With other words we call various APIs to collect data and statistics about many aspects of the programming process.

In this task we ask you to design an API endpoint that connects to the public [SWAPI api](https://swapi.dev/). 
It's an API dedicated to the Star Wars movies. Among other things the SW API exposes the URL `/vehicles`, 
where they return all vehicles from all SW films.

We would like you to implement the endpoint that accepts 1 user parameter: `minimal_cargo_capacity` and then lists
all vehicles from the Star Wars movies that have at least this much cargo capacity. For each vehicle we wish to see
the following information:

- Vehicle Name
- Vehicle Model
- Cargo Capacity

Return a **JSON response**, don't build any UI templates or frontend applications.

## Expectations

- this task should take you around 30 minutes to solve
- no tests: definitely don't write any e2e or integration tests, but you are free to write unit tests if you feel like they will help you solve the task
- we do not expect fully production ready code, but try to use best practices when designing large, scalable web applications as much as possible given the time restriction
- no UI, just an API that returns a JSON response

You are free to re-design and refactor everything (add additional dependencies, class and files names), but we expect to be able to run your solution as described below.
If you are not comfortable using Python or this template, you are free to choose whichever language you are most comfortable with.
We only ask that you still run it in docker and we are able to run your solution with a single command. We explain code structure of the template later in this document.


## Getting started

You only need to have Docker installed.

### Build & Launch

Bring the dev environment up with
```bash
docker-compose up
```

This will expose the Flask application's endpoints on port `5001`.

To shut down:

```bash
docker-compose down
```

### Code structure

This template provides a simple Flask API.

- all the routes are defined in `api/app.py`, there you will find a couple demo endpoints and the one we expect you to implement
- we have provided a simple `SWApi` REST client in `api/swapi.py` that provides a `get` method.
