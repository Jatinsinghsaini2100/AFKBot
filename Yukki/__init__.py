import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

bot_id = 0
bot_name = ""
bot_username = ""

clean_mode = {}

SUDOERS = config.SUDO_USER

app = Client(
    ":YukkiAFKBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

async def initiate_bot():
    global bot_id, bot_name, bot_username
    try:
        await app.start()
        get_me = await app.get_me()
        bot_id = get_me.id
        bot_username = get_me.username.lower()
        if get_me.last_name:
            bot_name = f"{get_me.first_name} {get_me.last_name}"
        else:
            bot_name = get_me.first_name
    except Exception as e:
        print(f"Error occurred during bot initialization: {e}")

loop.run_until_complete(initiate_bot())
