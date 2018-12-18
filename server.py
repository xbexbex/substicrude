import requests
from flask import Flask, request
from os import environ
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
BOT_KEY = environ.get("BOT_KEY")
SECRET_PATH = environ.get("SECRET_PATH")

app = Flask(__name__)


@app.route('/')
def index():
    print(request.headers)
    return(request.headers)


@app.route('/bot')
def print_bot():
    print("botttt " + request.headers)
    return("botttt " + request.headers)

@app.route('/' + SECRET_PATH)
def print_secret():
    print("segret " + request.headers)
    return("segret " + request.headers)


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
