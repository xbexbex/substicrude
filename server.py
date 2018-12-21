import requests
import asyncio
import os
from flask import Flask, request
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv(override=True)
BOT_KEY = os.getenv("BOT_KEY")
SECRET_PATH = os.getenv("SECRET_PATH")

app = Flask(__name__)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

@app.route('/')
def index():
    print(request.headers)
    return(str(request.headers))


@app.route('/bot')
def print_bot():
    print(str(SECRET_PATH))
    return(str(SECRET_PATH))

@app.route('/' + str(BOT_KEY), methods=['POST'])
def print_secret():
    print("segret " + str(request.data))
    return("segret " + str(request.headers))

if __name__ == "__main__":
    app.run(
        ssl_context=('scrub.pem', 'scrub.key'),
        host='0.0.0.0',
        port='8443'
    )


""" def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(BOT_KEY, method)

def process_message(update):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = "I can hear you!"
    r = requests.post(get_url("sendMessage"), data=data)

@app.route("/{}".format(BOT_KEY), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            process_message(update)
        return "ok!", 200 """
