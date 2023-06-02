import os

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
OWNER_ID = list(map(int, os.getenv("OWNER_ID").split()))
PREFIX = os.getenv("PREFIX", " . , : ; - ? *").split()
SESSION_STRING = os.getenv("SESSION_STRING")
MEMBERS = list(map(int, os.getenv("MEMBERS", "").split()))
LOG_GRP = int(os.getenv("LOG_GRP"))
