# -*- coding: utf-8 -*-
from config import settings
from flask import Flask, request
from pymessenger.bot import Bot
from lib.Constructor.facebookConstructor import FacebookConstructor

app = Flask(__name__)

bot = Bot(settings.FACEBOOK_ACCESS_TOKEN)

botConstructor = FacebookConstructor(
    helpFile=settings.BOT_HELP_FILE["facebook"],
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=settings.MESSAGE,
    shopData=settings.SHOPS,
    resultItemCount=settings.RESULT_ITEMS_COUNT["facebook"],
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

    print data
    if recipient_id and message:
        dataCategory = ''

        if message.find("__") != -1:
            dataCategory = message.split("__")[0]
            dataId = message.split("__")[1]

        if dataCategory == "SHOP":
            print dataId
            bot.send_generic_message(
                recipient_id,
                botConstructor.botSelectStore()
            )
        elif dataCategory == "CHOICE":
            bot.send_generic_message(
                recipient_id,
                botConstructor.botCaliberChoice()
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
        else:
            bot.send_button_message(
                recipient_id,
                "bla bla",
                botConstructor.botCommands()
            )
    
    return "ok", 200

if __name__ == "__main__":
    app.run(port=1024, debug=True)
