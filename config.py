# ©Dp_botz©




import os, re
import logging
from logging.handlers import RotatingFileHandler

id_pattern = re.compile(r'^.\d+$')

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6729268257:AAFmSqHjcf5zdBBMxZrT-f17GpYq9jrkgLc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20652787"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5dea928561e4d2eb77a371edf8b2eb2a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002011721546"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1242556540"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Aloneboy:Aloneboytg@cluster0.nmeelsr.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "mongodb")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002050387186"))


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions




TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello 👋 {first} 💙 I can store private files in Specified Channel and other users can access it from special link ✅ Developer @Dp_Botz")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1242556540").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "hello - {username} join my channel 👍 Next Click , Try again ✅ Developer channel @Dp_botz")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{previouscaption}\n\n𝐉ᴏɪɴ ➠ @AnimesWorldTamil ✅")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot! you need Own Bot Contact To My owner @Dpowner_bot"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = os.environ.get("REQ_CHANNEL", "-1002038571576")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = os.environ.get("JOIN_REQS_DB", DB_URI)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
