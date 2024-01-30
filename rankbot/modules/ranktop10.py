from pyrogram import Client, filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from rankbot import rankbot as app
from pyrogram.types import Message
from config import BOT_USERNAME, OWNER_ID
import asyncio
# -----------------




# --------------------------------------------------------------------------
mongo_uri = "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority"
database_name = "MONGODB"
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

mongo_client = MongoClient(mongo_uri)
db = mongo_client[database_name]
top_members_collection = db["rank_db"]

user_data = {}

# ----------------



@app.on_message(filters.command("top10"))
def top_members(_, message):
    top_members = top_members_collection.find().sort("total_messages", -1).limit(10)
    
    response = "📈 𝖫𝖤𝖠𝖣𝖤𝖱𝖡𝖮𝖠𝖱𝖣\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        
        try:
            user = app.get_users(user_id)
            Mention = user.mention if user.mention else "none"
        except PeerIdInvalid:
            first_name = "Unknown"
        
        total_messages = member["total_messages"]
        user_info = f"{idx}. 👤{Mention}, •{total_messages}\n"
        response += user_info

    message.reply_text(response)


@app.on_message()
def handle_messages(_, message):
    user_id = message.from_user.id
    
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1
    
    top_members_collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)

# ------------------------------


# --------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------

start_txt = """
**🤖 *𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳*

𝖧𝖤𝖫𝖫𝖮  \n\n👋 𝖨'𝖬 𝖸𝖮𝖴𝖱 𝖥𝖱𝖨𝖤𝖭𝖣𝖫𝖸 𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳. \n
🚀 𝖢𝖴𝖱𝖨𝖮𝖴𝖲 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖬𝖮𝖲𝖳 𝖠𝖢𝖩𝖨𝖵𝖤 𝖬𝖤𝖬𝖡𝖤𝖱𝖲?
𝖲𝖳𝖠𝖸 𝖳𝖴𝖭𝖤𝖣 𝖥𝖮𝖱 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖮𝖧 𝖬𝖤𝖲𝖲𝖠𝖦𝖨𝖭𝖦 𝖠𝖢𝖧𝖨𝖤𝖵𝖤𝖬𝖤𝖭𝖳𝖲!
𝖪𝖤𝖤𝖯 𝖳𝖧𝖮𝖲𝖤 𝖢𝖮𝖭𝖵𝖤𝖱𝖲𝖠𝖳𝖨𝖮𝖭𝖲 𝖥𝖫𝖮𝖶𝖨𝖭𝖦. 🚀✨!**
"""
# --------------------------------------------------------------------------------
@app.on_message(filters.command("start")& filters.private)
async def start(_, msg):
    start_txt = (
        "🤖 **𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳**\n\n"
        "**𝖧𝖤𝖫𝖫𝖮**  \n\n👋 **𝖨'𝖬 𝖸𝖮𝖴𝖱 𝖥𝖱𝖨𝖤𝖭𝖣𝖫𝖸 𝖱𝖠𝖭𝖪𝖨𝖭𝖦 𝖡𝖮𝖳.**\n"
        "🚀 **𝖢𝖴𝖱𝖨𝖮𝖴𝖲 𝖠𝖡𝖮𝖴𝖳 𝖳𝖧𝖤 𝖬𝖮𝖲𝖳 𝖠𝖢𝖩𝖨𝖵𝖤 𝖬𝖤𝖬𝖡𝖤𝖱𝖲?**\n"
        "**𝖲𝖳𝖠𝖸 𝖳𝖴𝖭𝖤𝖣 𝖥𝖮𝖱 𝖴𝖯𝖣𝖠𝖳𝖤𝖲 𝖮𝖧 𝖬𝖤𝖲𝖲𝖠𝖦𝖨𝖭𝖦 𝖠𝖢𝖧𝖨𝖤𝖵𝖤𝖬𝖤𝖭𝖳𝖲!**\n"
        "**𝖪𝖤𝖤𝖯 𝖳𝖧𝖮𝖲𝖤 𝖢𝖮𝖭𝖵𝖤𝖱𝖲𝖠𝖳𝖨𝖮𝖭𝖲 𝖥𝖫𝖮𝖶𝖨𝖭𝖦. 🚀✨!**"
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
    
    await msg.reply_photo(
        photo="https://graph.org/file/f77b368fdbc1431973c36.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
    
