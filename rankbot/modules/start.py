from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import Message
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from rankbot import rankbot as app
import config
from config import OWNER_ID, BOT_TOKEN
# --------------------------------------------------------------------------


start_txt = """
**🤖 *𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳*

𝖧𝖤𝖫𝖫𝖮 {}! \n\n👋 𝖨'𝖬 𝖸𝖮𝖴𝖱 𝖥𝖱𝖨𝖤𝖭𝖣𝖫𝖸 𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳. \n
🚀 𝖢𝖴𝖱𝖨𝖮𝖴𝖲 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖬𝖮𝖲𝖳 𝖠𝖢𝖳𝖨𝖵𝖤 𝖬𝖤𝖬𝖡𝖤𝖱𝖲?
𝖲𝖳𝖠𝖸 𝖳𝖴𝖭𝖤𝖣 𝖥𝖮𝖱 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖮𝖭 𝖬𝖤𝖲𝖲𝖠𝖦𝖨𝖭𝖦 𝖠𝖢𝖧𝖨𝖤𝖵𝖤𝖬𝖤𝖭𝖳𝖲!
𝖪𝖤𝖤𝖯 𝖳𝖧𝖮𝖲𝖤 𝖢𝖮𝖭𝖵𝖤𝖱𝖲𝖠𝖳𝖨𝖮𝖭𝖲 𝖥𝖫𝖮𝖶𝖨𝖭𝖦. 🚀✨!**
"""
# --------------------------------------------------------------------------------
@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
            InlineKeyboardButton("➕𝖠𝖣𝖣 𝖬𝖤 𝖨𝖭 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🆘𝖲𝖴𝖯𝖯𝖮𝖱𝖳🆘", url="https://t.me/DAXXSUPPORT"),
            InlineKeyboardButton("🧑‍💻𝖣𝖤𝖵🧑‍💻", user_id=OWNER_ID)
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/f77b368fdbc1431973c36.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
