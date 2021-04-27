from py4web import URL, abort, action, redirect, request

from . import dummy
from .fixtures import auth, db, session, url_signer
from .utils import get_user


# ==== pages ====
@action("index")
@action.uses("index.html", db, session, auth)
def index():
    user = get_user()
    owned_sessions = None
    signed_up_sessions = None

    if user is not None:
        owned_sessions = list(db(db.game_sessions.owner_id == user.id).select())
        signed_up_sessions = []

        for signup in db(db.game_signups.user_id == user.id).iterselect():
            game_session = db.game_sessions[signup.session_id]
            if game_session.owner_id != user.id:  # if we own the session, it's already in owned_sessions
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
    return {"user": get_user()}


@action('sessions/<session_id:int>')
@action.uses("sessions/view.html", db, session, auth)
def view_session(session_id):
    return {"user": get_user()}


@action('sessions/<session_id:int>/edit')
@action.uses("sessions/edit.html", db, session, auth)
def edit_session(session_id):
    # user must have permission to edit session, session must exist
    # user = get_user()
    # game_session = db.game_sessions[session_id]
    # if game_session is None or game_session.owner_id != user.id:
    #     abort(404, "Session not found")
    # return {"user": user, "session": game_session}
    return {"user": get_user(), "session": dummy.full_session}  # todo uncomment the above to use real data


@action('sessions/<session_id:int>/edit_signup/<signup_id:int>')
@action.uses("sessions/edit_signup.html", db, session, auth)
def edit_signup(session_id, signup_id):
    game_session = db.game_sessions[session_id]
    signup = db.game_signups[signup_id]
    user = get_user()
    if game_session is None or signup is None:
        abort(404, "Signup not found")

    # if the signup is from a user,

    return {"user": user}


@action('sessions/<session_id:int>/join')
@action.uses(db, session, auth, url_signer.verify())
def join_session(session_id):
    """after user confirm @ invite - verify join action, create signup, then redir to edit signup"""
    user = get_user()  # may not exist if anonymous - check query for anonymous name
    query = request.query

    # if user is not logged in and name is not passed to qstring, abort
    if not (user or query.get('name')):
        abort(400, "Expected login or name")

    # get game session
    game_session = db.game_sessions[session_id]
    if game_session is None:
        abort(404, "Game session not found")

    # check if there's already a signup (if so, redir to edit)
    if user:
        existing_signup = db(db.game_signups.session_id == session_id,
                             db.game_signups.user_id == user.id).select().first()
    else:
        existing_signup = db(db.game_signups.session_id == session_id,
                             db.game_signups.anonymous_name == query['name']).select().first()

    if existing_signup is not None:
        redirect(URL(f"sessions/{session_id}/edit_signup/{existing_signup.id}"))

    # create a new signup and redir to edit
    if user:
        new_signup_id = db.game_signups.insert(session_id=session_id, user_id=user.id)
    else:
        new_signup_id = db.game_signups.insert(session_id=session_id, anonymous_name=query['name'])
    redirect(URL(f"sessions/{session_id}/edit_signup/{new_signup_id}"))


@action('invite/<invite_key>')
@action.uses("sessions/invite.html", db, session, auth)
def invite(invite_key):
    user = get_user()
    # get the invite with the corresponding key
    # game_invite = db(db.game_invites.key == invite_key).select().first()
    # if game_invite is None:
    #     abort(404, "Invalid invite")
    # game_session = db.game_sessions[game_invite.session_id]
    # existing_signup = None
    # if user:
    #     existing_signup = db(db.game_signups.session_id == game_invite.session_id,
    #                          db.game_signups.user_id == user.id).select().first()
    # return {
    #     "user": user,
    #     "url_signer": url_signer,
    #     "session": game_session,
    #     "existing_signup": existing_signup
    # }

    # build the page with the session the invite points to
    return {
        "user": user,
        "url_signer": url_signer,
        "session": dummy.session2,
        "existing_signup": False
    }


# ==== API ====

# ==== dev test ====
# todo remove me
@action('test/vue')
@action.uses("test/vue.html", db, session, auth)
def test_vue():
    user = get_user()
    return {"user": user}
