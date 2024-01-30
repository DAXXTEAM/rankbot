import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_USERNAME, OWNER_ID




loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



rankbot = Client(
    ":rankbot:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)



async def rankbot_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await rankbot.start()
    getme = await rankbot.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(rankbot_bot())
