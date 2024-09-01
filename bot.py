import os
import asyncio
from pyrogram import Client, filters, idle

API_ID = int(os.getenv("API_ID", "22703591"))
API_HASH = os.getenv("API_HASH", "c24dc1c63e09d82947dc9b143eb079fc")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7179483692:AAGhhLgWlIsO4rWTP9Vfc_Dq56ddWj8elaM")
SESSION = os.getenv("SESSION", "BQFabecAV9n9-hFsUruLvyf5iRHK76DtoGx5OMDzRzmNtKowjms896TjfitRtiOVwpW5lyrBXRgvAib4K2ANAWLMggJs_rokxob1EAE-JTS7hcE_wnISrUzAXOwGPv0Iy3xjdOcC8rGJhlZ-8kWtVD9hFFqTFot95LGQITp0qNZ1tr2KrlsoS8-LYLNsBe0qtiUqpFXUaf23Z4xmZ0h4W0gbiksuJcZOcsHZcSruUd1R58mPCuZOynn-wqKKlAyTBOQmglwNq51eM7kbHiLVO-tnwZT4514Ow1kAZ86ENunYGXSlzLu4aisZ7iThhbqJal3QBU_4Vh6sSA9QI1gjtUchOq4RpgAAAAGiUGwDAA")
TIME = int(os.getenv("TIME", 5))

GROUPS = list(map(int, os.getenv("GROUPS", "1 0 0 2 0 8 8 7 2 1 0 1 9").split()))
ADMINS = list(map(int, os.getenv("ADMINS", "1527277551").split()))

START_MSG = "<b>Hello {},\n\nI'm a groups messages delete bot after a specific time.\n\nWorking for my owner groups.</b>"

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )

Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
        if message.from_user.id in ADMINS:
            return
        else:
            await asyncio.sleep(TIME)
            await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
        print(f"Error occurred in delete function: {e}")

try:
    User.start()
    print("User Started!")
    Bot.start()
    print("Bot Started!")
    idle()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    User.stop()
    print("User Stopped!")
    Bot.stop()
    print("Bot Stopped!")
