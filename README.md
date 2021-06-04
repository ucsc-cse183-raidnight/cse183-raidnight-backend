# cse183-raidnight-backend

Backend for raidnight.

## Requirements

- Python 3.8+

## Setup

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Running

``py4web run apps``

## Deploying

First, make a file named ``secrets.yaml`` containing the environment vars needed (see ``apps/raidnight/config.py``)

``gcloud app deploy``

