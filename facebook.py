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

    if recipient_id and message:
        dataCategory = ''

        if message.find("__") != -1:
            dataCategory = message.split("__")[0]
            dataId = message.split("__")[1]

        if dataCategory == "SHOP":
            bot.send_generic_message(
                recipient_id,
                botConstructor.botInitTop()
            )
        elif dataCategory == "TOP":
            textArray, link = botConstructor.botPrintTop(dataId)
            textFormated = botConstructor.separateText(textArray)

            if len(textFormated) >= 640:
                lenArr = len(textArray)

                textPartFirst = botConstructor.separateText(textArray[:lenArr / 2])
                textPartSecond = botConstructor.separateText(textArray[lenArr / 2:])

                bot.send_text_message(
                    recipient_id,
                    textPartFirst
                )
                textFormated = textPartSecond
                    
            bot.send_button_message(
                recipient_id,
                textFormated,
                botConstructor.createButtonLink(
                    settings.MESSAGE["link_text"],
                    link
                )
            )
        elif dataCategory == "DISCOUNT":
            pass
        else:
            bot.send_generic_message(
                recipient_id,
                botConstructor.botSelectStore()
            )
    
    return "ok", 200

if __name__ == "__main__":
    app.run(port=1024, debug=True)
