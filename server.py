import requests
import os
import json
import asyncio
from quart import Quart, request
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv(override=True)
BOT_KEY = os.getenv("BOT_KEY")
SECRET_PATH = os.getenv("SECRET_PATH")
BOT_ID = os.getenv("BOT_ID")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

app = Quart(__name__)
loop = asyncio.get_event_loop()

@app.route('/')
def index():
    print(request.headers)
    return(str(request.headers))


@app.route('/bot')
def print_bot():
    print(str(SECRET_PATH))
    return(str(SECRET_PATH))


@app.route('/' + str(BOT_KEY), methods=['POST'])
def webhook_receive():
    print("segret " + str(request.data))
    data = json.loads(request.data)
    print(request.data)
    if 'new_chat_participant' in data['message']:
        if str(data['message']['new_chat_participant']['id']) == str(BOT_ID):
            new_chat_action(data['message']['chat']['id'])
    return("segret " + str(request.headers))


@app.route('/chat', methods=['GET'])
def get_chat_data():
    id = request.args.get('id')
    client = TelegramClient('session_name', API_ID, API_HASH)
    loop.run_until_complete(client.start())
    return("ddd")


def new_chat_action(id: int):
    print(id)


if __name__ == "__main__":
    app.run(
        certfile='scrub.pem', 
        keyfile='scrub.key',
        host='0.0.0.0',
        port='8443',
        debug=1
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
