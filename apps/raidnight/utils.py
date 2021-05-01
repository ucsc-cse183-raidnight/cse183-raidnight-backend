import secrets

from py4web import response

from .fixtures import auth
from .schemas import DiscordUser, GameSessionFull, GameSessionRole, GameSessionRule


# ---- api utils ----
def success(data, code=200):
    response.status = code
    return {"success": True, "data": data}


def error(code, reason):
    response.status = code
    return {"success": False, "error": reason}


# ---- other utils ----
def get_user():
    """Gets the user as a Pydantic model instead of a dict. Returns None if no user is logged in."""
    user = auth.get_user()
    if not user:
        return None
    return DiscordUser(id=user['id'], username=user['username'], email=user['email'], avatar_hash=user['last_name'])


def generate_invite_key():
    return secrets.token_urlsafe(5)


def get_game_session_full(db, session_id):
    session = db.game_sessions[session_id]
    if session is None:
        return None

    if session.owner_id is not None:
        owner_data = db.auth_user[session.owner_id]
        owner = DiscordUser(id=owner_data.id, username=owner_data.username, email=owner_data.email,
                            avatar_hash=owner_data.last_name)
    else:
        owner = None

    roles = []
    all_roles = []
    all_rules = []

    def recursive_load_roles(role_data):
        role_id = role_data.id
        role = GameSessionRole(id=role_id, session_id=session_id, name=role_data.name,
                               parent_id=role_data.parent_id, icon=role_data.icon, children=[], rules=[])

        for rule_data in db(db.game_rules.session_id == session_id and db.game_rules.role_id == role_id).select():
            rule = GameSessionRule(id=rule_data.id, session_id=session_id, role_id=role_id,
                                   operator=rule_data.rule_operator, value=rule_data.rule_value)
            role.rules.append(rule)
            all_rules.append(rule)

        for child_data in db(db.game_roles.session_id == session_id and db.game_roles.parent_id == role_id).select():
            role.children.append(recursive_load_roles(child_data))
        all_roles.append(role)
        return role

    # noinspection PyComparisonWithNone
    for rd in db(db.game_roles.session_id == session_id and db.game_roles.parent_id == None).select():
        roles.append(recursive_load_roles(rd))

    return GameSessionFull(
        id=session.id,
        name=session.name,
        description=session.description,
        owner=owner,
        selected_time_offset=session.selected_time_offset,
        selected_time_duration=session.selected_time_duration,
        selected_time_timezone=session.selected_time_timezone,
        roles=roles,
        all_roles=all_roles,
        all_rules=all_rules
    )
