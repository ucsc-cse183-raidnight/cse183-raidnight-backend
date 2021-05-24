import secrets

from py4web import response

from .fixtures import auth
from .schemas import DiscordUser, GameSessionFull, GameSessionRole, GameSessionRule, GameSignupFull, SignupRole, \
    SignupTime


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


def get_user_by_id(db, user_id):
    if user_id is None:
        return None
    user_data = db.auth_user[user_id]
    return DiscordUser(id=user_data.id, username=user_data.username, email=user_data.email,
                       avatar_hash=user_data.last_name)


def get_game_session_full(db, session_id):
    session = db.game_sessions[session_id]
    if session is None:
        return None

    owner = get_user_by_id(db, session.owner_id)
    roles = []
    all_roles = []
    all_rules = []

    session_role_rows = db(db.game_roles.session_id == session_id).select()
    session_rule_rows = db(db.game_rules.session_id == session_id).select()

    def recursive_load_roles(role_data):
        role_id = role_data.id
        role = GameSessionRole(id=role_id, session_id=session_id, name=role_data.name,
                               parent_id=role_data.parent_id, icon=role_data.icon, children=[], rules=[])

        for rule_data in session_rule_rows.find(lambda r: r.role_id == role_id):
            rule = GameSessionRule(id=rule_data.id, session_id=session_id, role_id=role_id,
                                   operator=rule_data.rule_operator, value=rule_data.rule_value)
            role.rules.append(rule)
            all_rules.append(rule)

        for child_data in session_role_rows.find(lambda r: r.parent_id == role_id):
            role.children.append(recursive_load_roles(child_data))
        all_roles.append(role)
        return role

    for rd in session_role_rows.find(lambda r: r.parent_id is None):
        roles.append(recursive_load_roles(rd))

    invite = db(db.game_invites.session_id == session_id).select().first()
    if invite is None:
        invite_key = generate_invite_key()
        db.game_invites.insert(session_id=session_id, key=invite_key)
    else:
        invite_key = invite.key

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
        all_rules=all_rules,
        invite_key=invite_key
    )


def get_game_signup_full(db, signup_id):
    signup = db.game_signups[signup_id]
    if signup is None:
        return None

    user = get_user_by_id(db, signup.user_id)
    times = []
    roles = []

    for time_data in db(db.game_signup_times.signup_id == signup_id).select():
        times.append(SignupTime.parse_obj(time_data))

    for role_data in db(db.game_signup_roles.signup_id == signup_id).select():
        roles.append(SignupRole.parse_obj(role_data))

    return GameSignupFull(
        id=signup_id,
        user=user,
        anonymous_name=signup.anonymous_name,
        times=times,
        roles=roles
    )
