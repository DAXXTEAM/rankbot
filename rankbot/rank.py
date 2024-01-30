from pyrogram import Client, Filters
from collections import defaultdict
import datetime

# Initialize Pyrogram client
api_id = "your_api_id"
api_hash = "your_api_hash"
bot_token = "your_bot_token"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Dictionary to store daily and overall message counts for each user in each group
group_data = defaultdict(lambda: defaultdict(int))

# Function to update message count for a user in a group
def update_message_count(chat_id, user_id):
    group_data[chat_id][user_id] += 1

# Function to get top members in a group
def get_top_members(chat_id):
    return sorted(group_data[chat_id].items(), key=lambda x: x[1], reverse=True)[:10]

# Function to display top members in a group
def display_top_members(bot, update):
    chat_id = update.chat.id
    top_members = get_top_members(chat_id)
    message = "Top 10 Members in this Group:\n"
    for i, (user_id, message_count) in enumerate(top_members, start=1):
        message += f"{i}. User ID: {user_id}, Messages: {message_count}\n"
    bot.send_message(chat_id, message)

# Function to handle /rankings command
@app.on_message(Filters.command("rankings", prefixes="/"))
def handle_rankings_command(bot, update):
    chat_id = update.chat.id
    top_members = get_top_members(chat_id)
    message = "Top 10 Members in this Group:\n"
    for i, (user_id, message_count) in enumerate(top_members, start=1):
        message += f"{i}. User ID: {user_id}, Total Messages: {message_count}\n"
    bot.send_message(chat_id, message)

# Function to handle incoming messages
@app.on_message(Filters.group)
def handle_message(bot, update):
    chat_id = update.chat.id
    user_id = update.from_user.id
    update_message_count(chat_id, user_id)

# Function to reset daily message count
def reset_daily_count():
    now = datetime.datetime.now()
    for chat_id in group_data.keys():
        group_data[chat_id] = defaultdict(int)
    print(f"Daily counts reset at {now}")

# Schedule daily reset of message counts
scheduler = AsyncIOScheduler()
scheduler.add_job(reset_daily_count, 'cron', hour=0, minute=0)
scheduler.start()

# Start the bot
app.run()
