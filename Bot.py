import os
import logging
import asyncio
from telethon import TelegramClient, events, Button
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator, ChannelParticipantsAdmins
from telethon.errors import UserNotParticipantError
from flask import Flask
from threading import Thread

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s")
LOGGER = logging.getLogger(__name__)

# Environment Variables
api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")

# Initialize Telegram Client
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

# Flask Server Initialization
app = Flask(__name__)

@app.route('/')
def home():
    return "Shivi Mention Bot is Running!"

@app.route('/ping')
def ping():
    return "PONG"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Start Flask in a separate thread
Thread(target=run_flask).start()

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")

    await event.client.send_file(
        event.chat_id,
        file="https://i.ibb.co/BHDbt7dT/IMG-20250206-194914-423.jpg",
        caption="━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ ɪ ᴀᴍ sᴡᴇᴇᴛʏ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ\n✪ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʀᴜɴ /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ ᴏᴡɴᴇʀ    : [sᴡᴇᴇᴛʏ ʙᴏᴛ](https://t.me/rishu1286)\n┣★ ᴜᴘᴅᴀᴛᴇs › : [sᴡᴇᴇᴛʏ ʜᴇʟᴘ](https://t.me/ur_rishu_143)\n┣★ ᴜᴘᴅᴀᴛᴇ › : [ᴄʜᴀɴɴᴇʟ](https://t.me/vip_robotz/)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ\nᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/rishu1286) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=[
            [Button.url("❤️‍🔥 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 💫", "https://t.me/ShiviBOT?startgroup=true")],
            [Button.url("❤️‍🔥 ɢʀᴏᴜᴘ 💫", "t.me/ur_rishu_143"), Button.url("❤️‍🔥 ᴄʜᴀɴɴᴇʟ 💫", "https://t.me/vip_robotz")]
        ]
    )

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if event.chat_id not in spam_chats:
        return await event.respond("ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("sᴛᴏᴘᴘᴇᴅ.")

print(">> SHIVI MENTION BOT WORKING <<")
client.run_until_disconnected()
