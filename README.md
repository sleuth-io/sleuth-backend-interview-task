# Sleuth backend interview task

Hello, this is Sleuth backend interview task. <something about as you probably know we have lots of integrations, blah, blah>

We ask you to design an API that will enable our users to:
list PRs of any Github repository (public and private). Each PR needs to have the following:
   1. PR title
   2. PR author
   3. Number of commits in the PR
   4. Number of comments on the PR
   5. Head sha of the PR
   6. Last time the PR was updated

We do not expect any UI: a JSON response is ok.  

You are free to re-design and refactor everything, but we expect to be able to run your solution as described below. 


### Installation

You only need to have Docker installed.

### Build & Launch

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
