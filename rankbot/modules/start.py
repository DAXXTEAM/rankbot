from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import BOT_USERNAME, OWNER_ID
from rankbot import rankbot as app
import asyncio

# --------------------------------------------------------------------------

start_txt = """
**🤖 *𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳*

𝖧𝖤𝖫𝖫𝖮  \n\n👋 𝖨'𝖬 𝖸𝖮𝖴𝖱 𝖥𝖱𝖨𝖤𝖭𝖣𝖫𝖸 𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳. \n
🚀 𝖢𝖴𝖱𝖨𝖮𝖴𝖲 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖬𝖮𝖲𝖳 𝖠𝖢𝖩𝖨𝖵𝖤 𝖬𝖤𝖬𝖡𝖤𝖱𝖲?
𝖲𝖳𝖠𝖸 𝖳𝖴𝖭𝖤𝖣 𝖥𝖮𝖱 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖮𝖧 𝖬𝖤𝖲𝖲𝖠𝖦𝖨𝖭𝖦 𝖠𝖢𝖧𝖨𝖤𝖵𝖤𝖬𝖤𝖭𝖳𝖲!
𝖪𝖤𝖤𝖯 𝖳𝖧𝖮𝖤𝖤 𝖢𝖮𝖭𝖵𝖤𝖱𝖲𝖠𝖳𝖨𝖮𝖭𝖲 𝖥𝖫𝖮𝖶𝖨𝖭𝖦. 🚀✨!**
"""
# --------------------------------------------------------------------------------
@app.on_message(filters.command("start")& filters.private)
async def start(_, message):
    start_txt = (
        "🤖 **𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳**\n\n"
        "**𝖧𝖤𝖫𝖫𝖮**  \n\n👋 **𝖨'𝖬 𝖸𝖮𝖴𝖱 𝖥𝖱𝖨𝖤𝖭𝖣𝖫𝖸 𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳.**\n"
        "🚀 **𝖢𝖴𝖱𝖨𝖮𝖴𝖲 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖬𝖮𝖲𝖳 𝖠𝖢𝖩𝖨𝖵𝖤 𝖬𝖤𝖬𝖡𝖤𝖱𝖲?**\n"
        "**𝖲𝖳𝖠𝖸 𝖳𝖴𝖭𝖤𝖣 𝖥𝖮𝖱 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖮𝖧 𝖬𝖤𝖲𝖲𝖠𝖦𝖨𝖭𝖦 𝖠𝖢𝖧𝖨𝖤𝖵𝖤𝖬𝖤𝖭𝖳𝖲!**\n"
        "**𝖪𝖤𝖤𝖯 𝖳𝖧𝖮𝖤𝖤 𝖢𝖮𝖭𝖵𝖤𝖱𝖲𝖠𝖳𝖨𝖮𝖭𝖲 𝖥𝖫𝖮𝖶𝖨𝖭𝖦. 🚀✨!**"
    )

    buttons = [
        [ 
            InlineKeyboardButton("➕𝖠𝖣𝖣 𝖬𝖤 𝖨𝖭 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🆘𝖲𝖴𝖯𝖱𝖮𝖳🆘", url="https://t.me/DAXXSUPPORT"),
            InlineKeyboardButton("🧑‍💻𝖣𝖤𝖵🧑‍💻", user_id=OWNER_ID)
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await message.reply_photo(
        photo="https://graph.org/file/f77b368fdbc1431973c36.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
