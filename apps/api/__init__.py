from py4web import action


@action('hello')
def hello():
    return {"success": True, "world": "hello"}