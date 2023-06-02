import sys
from typing import Callable
import asyncio
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyromod import listen

from .config import *

LOOP = asyncio.get_event_loop()

CMD_HELP = {}

if not API_ID:
    print("API_ID Tidak ada")
    sys.exit()

if not API_HASH:
    print("API_HASH Tidak ada")
    sys.exit()

if not BOT_TOKEN:
    print("BOT_TOKEN Tidak ada")
    sys.exit()

if not LOG_GRP:
    print("LOG_GRP Tidak ada")
    sys.exit()

if not MONGO_URL:
    print("MONGO_URL Tidak ada")
    sys.exit()

if not SESSION_STRING:
    print("SESSION_STRING Tidak ada")
    sys.exit()


bot = Client(
    name="XadegaUserbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None, group=0):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._ubot:
            self._ubot.append(self)


ubot = Ubot(
    name="ubot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)
