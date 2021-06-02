import os

SESSION_SECRET = os.getenv("SESSION_SECRET")
DB_URI = os.getenv("DB_URI", 'sqlite://dev.db')

DISCORD_CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
DISCORD_CLIENT_SECRET = os.getenv("DISCORD_CLIENT_SECRET")
