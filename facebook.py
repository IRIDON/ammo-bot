# -*- coding: utf-8 -*-
from config import settings
from flask import Flask, request
from pymessenger.bot import Bot
from lib.Constructor.facebookConstructor import FacebookConstructor

app = Flask(__name__)

bot = Bot(settings.FACEBOOK_ACCESS_TOKEN)

botConstructor = FacebookConstructor(
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=settings.MESSAGE,
    shopData=settings.SHOPS,
    resultItemCount=settings.RESULT_ITEMS_COUNT,
)

@app.route("/", methods=['GET'])
def verify():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == settings.FACEBOOK_VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

@app.route("/", methods=['POST'])
def webhook():
    data = request.get_json()
    recipient_id, message = botConstructor.getMessage(data)
    keyboard = botConstructor.botSelectStore()

    for itemKeyboard in keyboard:
        bot.send_button_message(
            recipient_id,
            message,
            itemKeyboard
        )


    return "ok", 200

if __name__ == "__main__":
    app.run(port=1024, debug=True)
