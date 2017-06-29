# -*- coding: utf-8 -*-
import json
from config import settings
from flask import Flask, request
from pymessenger.bot import Bot
from lib.Constructor.facebookConstructor import FacebookConstructor

app = Flask(__name__)
bot = Bot(settings.FACEBOOK_ACCESS_TOKEN)

def readDataFile(dataFile):
    with open(dataFile, "r") as dataFile:
        data = json.loads(dataFile.read())

        return data["message"], data["commands"]

dataMessage, dataCommands = readDataFile(settings.BOT_DATA_FILE)

botConstructor = FacebookConstructor(
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=dataMessage,
    commands=dataCommands,
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

    if recipient_id and message:
        dataCategory = ''

        if message.find("__") != -1:
            dataCategory = message.split("__")[0]
            dataId = message.split("__")[1]

            # print dataCategory
            # print dataId

        if dataCategory == "SHOP":
            if dataId == "DISCOUNT":
                bot.send_generic_message(
                    recipient_id,
                    botConstructor.printListDiscount()
                )
            else:
                bot.send_generic_message(
                    recipient_id,
                    botConstructor.botSelectStore()
                )
        elif dataCategory == "DISCOUNT":
            botConstructor.setDiscount(dataId)
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
                    dataMessage["link_text"],
                    link
                )
            )
        else:
            bot.send_button_message(
                recipient_id,
                dataMessage["select_commad"],
                botConstructor.botCommands()
            )
    
    return "ok", 200

if __name__ == "__main__":
    app.run(port=1024, debug=True)
