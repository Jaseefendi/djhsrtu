from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
API_ID = int(getenv("API_ID", "21176306"))
API_HASH = getenv("API_HASH", "2edd5e2ff51741e893b6cb08a67558b5")
BOT_TOKEN = getenv("BOT_TOKEN", "7354357016:AAEwbF5lpfhwlHmd7ZUo1sY3Z8ph_i_HD6g")
BOT_NAME = getenv("BOT_NAME", "Quatra Music Bot") 
BOT_USERNAME = getenv("BOT_USERNAME", "QuatraMusicBot")
BOT_CHANNEL = getenv("BOT_CHANNEL", "QuatraDuyuru")
ASS_USERNAME = getenv("ASS_USERNAME", "Quatra Music Asistan")
OWNER = getenv("OWNER", "YuceEfendi")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6181368568").split()))
