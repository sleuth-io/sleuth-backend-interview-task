# Sleuth backend interview task

Hello, and welcome to backend interview task :wave:

At Sleuth we integrate with many providers and gather useful information that help our customers track engineering efficiency.
One of the basic integrations we have is integrating with various code source providers (Github, Gitlab, Bitbucket, etc.).
This task is designed so you get a feeling about what kind of problems you might be solving at Sleuth.

In this task we ask you to design an API that will enable our users to:
list **open** PRs of any public Github repository. For each PR we want to display only the following information:

- PR title
- username of the PR author
- Number of commits in the PR 
- Head sha of the PR
- Last time the PR was updated

Return a JSON response, don't build any UI templates or frontend applications.

## Expectations

- this task should take you around 30 minutes to solve
- the response should respect `page` and `per_page` query parameters and indicate if all available PRs from Github are included in the response
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
- we have provided a simple `GithubREST` client in `api/github.py` that provides a `get` method.
- `query_params.py` includes a very simple parsing of request query parameters, that your API implementation needs to respect
