from py4web import action

from .fixtures import auth, db, session


@action("index")
@action.uses("index.html", db, session, auth)
def index():
    user = auth.get_user()
    return dict(message="Hello {first_name}".format(**user) if user else "Hello")


@action('hello')
def hello():
    return {"success": True, "world": "hello"}
