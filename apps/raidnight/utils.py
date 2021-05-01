from py4web import response

from .fixtures import auth
from pydantic import BaseModel


class DiscordUser(BaseModel):
    id: int
    username: str
    email: str
    avatar_hash: str

    def __eq__(self, other):
        return self.id == other


def get_user():
    """Gets the user as a Pydantic model instead of a dict. Returns None if no user is logged in."""
    user = auth.get_user()
    if not user:
        return None
    return DiscordUser(id=user['id'], username=user['username'], email=user['email'], avatar_hash=user['last_name'])


# ---- api utils ----
def success(data, code=200):
    response.status = code
    return {"success": True, "data": data}


def error(code, reason):
    response.status = code
    return {"success": False, "error": reason}
