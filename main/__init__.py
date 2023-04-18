#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 10577960
API_HASH = "80fd047285f4e94ca80311928b6bb5da"
BOT_TOKEN = "6000243936:AAGzcwk8AoyUsz_WVMT7y9Avf3Lh6eR7_zw"
SESSION = "AQBDsDR2XDg5T7HP_-5eVVGOdMXIr0wu_V8dRjPaScJN0YB-Z3UuvIe8c-sedAIiTVbd5PiuUpvHT3S1lG9-W--1o_AYSjA9IYGmYVkSE6EZKkGa--aFTv3MPZzatwbLOlVU0RJ308Q3uEOzcW2ULtgSTaJ8OxEpRwn5GMklWCnIEznAwf3eLfDwom7exMtgzUVOW-CzLGJ9XrsbpJtujuYnu_0ivWks_7V0tT6L4ZsgljH3OD0T2kPhwcL270wfmzzJYa12QBvEx-iVV9Y7faRFmVpWmmm7I9WjloCQR1s0stGDTaMwszcP2T34_SfwrfD48wU2mKZpenW92LZjJhaxAAAAAU1mh7gA"
FORCESUB = "kdjiisb"
AUTH = 5593532344

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
