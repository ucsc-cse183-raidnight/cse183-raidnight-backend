"""
This file defines the necessary fixtures:

- the DAL (the py4web fixture) and necessary tables
- Session
- Auth

Note that it runs table definitions on import!
"""
import os

from py4web import DAL, HTTP, Session, URL, redirect
from py4web.utils.auth import Auth
from py4web.utils.auth_plugins import OAuth2
from py4web.utils.url_signer import URLSigner

from . import config

DB_FOLDER = os.path.join(os.path.dirname(__file__), '../../db')
db = DAL(config.DB_URI, folder=DB_FOLDER, pool_size=1, migrate=False, fake_migrate=False)
session = Session(secret=config.SESSION_SECRET)
url_signer = URLSigner(session)

########
# Auth #
########
auth = Auth(session, db, define_tables=False)
auth.use_username = True
auth.param.registration_requires_confirmation = False
auth.param.registration_requires_approval = False
auth.param.allowed_actions = ["logout"]  # deny most actions, since we only use Discord auth
auth.param.login_expiration_time = 60 * 60 * 24 * 30  # allow login for up to 1 month
auth.param.password_complexity = None  # we don't deal with passwords, only OAuth tokens!
auth.define_tables()


class OAuth2Discord(OAuth2):
    name = "oauth2discord"
    label = "Discord"

    login_url = "https://discord.com/api/oauth2/authorize"
    token_url = "https://discord.com/api/oauth2/token"
    userinfo_url = "https://discord.com/api/v8/users/@me"
    revoke_url = "https://discord.com/api/oauth2/token/revoke"
    default_scope = "identify email"
    maps = {
        "email": "email",
        "sso_id": "id",
        "first_name": "full_username",
        "last_name": "avatar",  # this is a hack
        "username": "full_username"
    }

    def callback(self, query):
        # since Discord returns username and discriminator separately, we extend the auth plugin's callback
        # function to merge them into a single field, so it can be mapped into username correctly later
        data = super().callback(query)
        data['full_username'] = f"{data['username']}#{data['discriminator']}"
        return data

    # in the source, it says this is unlikely to be needed to be overriden, but we need to override it, so...
    def _handle_callback(self, auth, get_vars):
        try:
            super()._handle_callback(auth, get_vars)
        except HTTP as e:
            # to redirect, py4web raises HTTP(303), which we can catch to suppress the redirect and do our own
            if e.status != 303:
                raise
        # redirect to where the user wanted to go, or index
        after = auth.session.get('after')
        if after is not None:
            redirect(URL(after))
        else:
            redirect(URL("index"))

    def handle_request(self, auth, path, get_vars, post_vars):
        if path == "login":
            # we can take a query param in the form of ?after=/invite/..., so save that to session to redirect
            # the user after a successful auth
            after = get_vars.get('after', 'index')
            auth.session['after'] = after
        super().handle_request(auth, path, get_vars, post_vars)


auth.register_plugin(
    OAuth2Discord(
        client_id=config.DISCORD_CLIENT_ID,
        client_secret=config.DISCORD_CLIENT_SECRET,
        callback_url="auth/plugin/oauth2discord/callback",
    )
)

auth.enable()
