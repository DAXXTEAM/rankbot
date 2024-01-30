from pyrogram import filters 
from rankbot import rankbot as app

db = {} 

@app.on_message(filters.group & group=11)
async def watcher(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    count += 1
    if user_id not in db["chat_id"]["user_id"]:
      user_data = {
      "user_id" : user_id,
      "first_name": first_name,
      "count": count,
      }
      db[chat_id] = user_data
    else:
      user_data = {
      "user_id" : user_id,
      "first_name": first_name,
      "count": count,
      }
      db[chat_id] = user_data
      print("user added !!")
      

    

    





@app.on_message(filters.command("top"))
async def ranks(_, message):
    chat_id = message.chat.id

    if chat_id in db and db[chat_id]:
        top_users = sorted(db[chat_id].values(), key=lambda x: x["message_count"], reverse=True)[:10]

        response = "Top 10 Users:\n"
        for rank, user_data in enumerate(top_users, start=1):
            response += f"{rank}. {user_data['first_name']} ({user_data['user_id']}) - {user_data['message_count']} messages\n"

        await message.reply_text(response)
    else:
        await message.reply_text("No data available.")



