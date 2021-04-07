from py4web import action

from . import fixtures

# todo remove me
# this is temporarily here to make py4web run the db migrations on startup
db = fixtures.db


@action('hello')
def hello():
    return {"success": True, "world": "hello"}
