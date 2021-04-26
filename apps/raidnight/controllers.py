from py4web import abort, action

from . import dummy
from .fixtures import auth, db, session, url_signer


# ==== pages ====
@action("index")
@action.uses("index.html", db, session, auth)
def index():
    user = auth.get_user()
    owned_sessions = None
    signed_up_sessions = None

    if user:
        owned_sessions = list(db(db.game_sessions.owner_id == user['id']).select())
        signed_up_sessions = []

        for signup in db(db.game_signups.user_id == user['id']).iterselect():
            game_session = db.game_sessions[signup.session_id]
            if game_session.owner_id != user['id']:  # if we own the session, it's already in owned_sessions
                signed_up_sessions.append(game_session)

        # todo remove me: dummy data
        owned_sessions.append(dummy.session1)
        signed_up_sessions.append(dummy.session2)
        signed_up_sessions.append(dummy.full_session)

    return {
        "user": user,
        "signed_up_sessions": signed_up_sessions,
        "owned_sessions": owned_sessions
    }


@action('sessions/new')
@action.uses("sessions/new.html", db, session, auth)
def create_session():
    return {"user": auth.get_user()}


@action('sessions/<session_id:int>')
@action.uses("sessions/view.html", db, session, auth)
def view_session(session_id):
    return {"user": auth.get_user()}


@action('sessions/<session_id:int>/edit')
@action.uses("sessions/edit.html", db, session, auth)
def edit_session(session_id):
    # user must have permission to edit session, session must exist
    # user = auth.get_user()
    # game_session = db.game_sessions[session_id]
    # if game_session is None or game_session.owner_id != user.get('id'):
    #     abort(404, "Session not found")
    # return {"user": user, "session": game_session}
    return {"user": auth.get_user(), "session": dummy.full_session}  # todo uncomment the above to use real data


@action('sessions/<session_id:int>/join')
@action.uses("sessions/join.html", db, session, auth, url_signer.verify())
def join_session(session_id):
    return {"user": auth.get_user()}


@action('invite/<invite_key>')
@action.uses("sessions/invite.html", db, session, auth)
def invite(invite_key):
    user = auth.get_user()
    # get the invite with the corresponding key
    # game_invite = db(db.game_invites.key == invite_key).select().first()
    # if game_invite is None:
    #     abort(404, "Invalid invite")
    # game_session = db.game_sessions[game_invite.session_id]
    # build the page with the session the invite points to
    return {"user": user, "session": dummy.session2, "url_signer": url_signer}

# ==== API ====
