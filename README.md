[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Instagrammers

Instagrammers is an instagram influencer search portal.

## Setup
Clone this repo
```bash
git clone git@github.com/roronoazor/instagrammers.git
```
Create a virtual environment using an env manager of your choice(virtualenv, conda, pipenv etc), activate your environment and install project requirements using `pip`

```bash
pip install -r requirements.txt
```

## Running

```bash
# run on port 8000 by default
uvicorn app.main:app
# visit 127.0.0.1:8000/docs
```
