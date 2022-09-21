# Sleuth backend interview task

Hello, and welcome to backend interview task :wave:

At Sleuth we integrate with many providers and gather useful information that help our customers track engineering efficiency.
One of the basic integrations we have is integrating with various code source providers (Github, Gitlab, Bitbucket, etc.).
This task is designed so you get a feeling about what kind of problems you might be solving at Sleuth.

In this task we ask you to design an API that will enable our users to:
list **open** PRs of any Github repository (public and private). For each PR we want to display only the following information:

- PR title
- PR author 
- Number of commits in the PR 
- Head sha of the PR
- Last time the PR was updated

## Expectations

- this task should take you around 30 minutes to solve
- no UI, just an API that returns a JSON response
- no tests: definitely don't write any e2e or integration tests, but you are free to write unit tests if you feel like they will help you solve the task
- we do not expect fully production ready code, but try to use best practices when designing large, scalable web applications

You are free to re-design and refactor everything (add additional dependencies, class and files names), but we expect to be able to run your solution as described below.
If you are not comfortable using Python or this template, you are free to choose whichever language you are most comfortable with.
We only ask that you still run it in docker and we are able to run your solution with a single command.


## Installation

You only need to have Docker installed.

## Build & Launch

Bring the dev environment up with
```bash
make up
```

This will expose the Flask application's endpoints on port `5001`.

To shut down:

```bash
make down
```

In order to make requests to private repositories, you will need to use your own Github personal access token.
You can create it [here](https://github.com/settings/tokens)
Then add it to `.env` file
```bash
cp .env.template .env
```
and set `GITHUB_API_TOKEN` variable. You will need to rerun `make up` for the change to have effect.
