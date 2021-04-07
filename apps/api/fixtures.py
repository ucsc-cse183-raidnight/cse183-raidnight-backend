"""
This file defines the necessary fixtures:

- the DAL (the py4web fixture) and necessary tables
- Session
- Auth

Note that it runs table definitions on import!
"""
import os

from py4web import DAL, Field, Session
from py4web.utils.auth import Auth

DB_FOLDER = os.path.join(os.path.dirname(__file__), '../../db')
db = DAL('sqlite://dev.db', folder=DB_FOLDER, pool_size=1)
session = Session(secret='my secret key')  # todo load secret from env var
auth = Auth(session, db)
auth.enable()

# ==== GAME ====
db.define_table(
    'game_sessions',  # not to be confused with sessions, the user kind
    Field('name', 'string', length=128, notnull=True),
    Field('description', 'text', length=2048, notnull=False),
    Field('owner_id', 'reference auth_user', notnull=False),  # can be null to signify anonymous owner
    Field('selected_time_offset', 'double', notnull=False),
    Field('selected_time_duration', 'double', notnull=False),
    Field('selected_time_timezone', 'string', notnull=False, length=512),
    # 1->X: game_signups
    # 1->X: game_invites
    # 1->X: game_roles
    # 1->X: game_rules
)

db.define_table(
    'game_signups',
    Field('user_id', 'reference auth_user', notnull=False),  # if null, anonymous_name must be not null
    Field('anonymous_name', 'string', length=128),  # mutex user_id
    Field('session_id', 'reference game_sessions', notnull=True)
    # 1->X: game_signup_times
    # 1->X: game_signup_roles
)

db.define_table(
    'game_signup_times',
    Field('signup_id', 'reference game_signups', notnull=True),
    Field('timezone', 'string', notnull=True, length=512),  # e.g. America/Los_Angeles
    Field('offset', 'double', notnull=True),
    Field('duration', 'double', notnull=True)
)

db.define_table(
    'game_signup_roles',
    Field('signup_id', 'reference game_signups', notnull=True),
    Field('role_id', 'reference game_roles', notnull=True),
    Field('weight', 'integer', notnull=True)
)

db.define_table(
    'game_invites',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('key', 'string', notnull=True, length=128)
)

db.define_table(
    'game_roles',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('name', 'string', notnull=True, length=128),
    Field('parent_id', 'reference game_roles'),
    Field('icon', 'string', length=128)
)

db.define_table(
    'game_rules',
    Field('session_id', 'reference game_sessions', notnull=True),
    Field('role_id', 'reference game_roles', notnull=True),
    Field('rule_type', 'string', notnull=True, length=64),
    Field('rule_operator', 'string', length=64),
    Field('rule_value', 'integer')
)

# ==== PRESETS ====
db.define_table(
    'game_presets',
    Field('name', 'string', notnull=True, length=128),
    Field('description', 'text', length=2048)
    # 1->X: game_preset_roles
    # 1->X: game_preset_rules
)

db.define_table(
    'game_preset_roles',
    Field('preset_id', 'reference game_presets', notnull=True),
    Field('name', 'string', notnull=True, length=128),
    Field('parent_id', 'reference game_preset_roles'),
    Field('icon', 'string', length=128)
)

db.define_table(
    'game_preset_rules',
    Field('preset_id', 'reference game_presets', notnull=True),
    Field('role_id', 'reference game_preset_roles', notnull=True),
    Field('rule_type', 'string', notnull=True, length=64),
    Field('rule_operator', 'string', length=64),
    Field('rule_value', 'integer')
)

db.commit()
