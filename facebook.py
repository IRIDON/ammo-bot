# -*- coding: utf-8 -*-
import json
from config import settings
from flask import Flask, request, render_template
from pymessenger.bot import Bot
from lib.Constructor.facebookConstructor import FacebookConstructor

app = Flask(__name__)
bot = Bot(settings.FACEBOOK["ACCESS_TOKEN"])

def readDataFile(dataFile):
    with open(dataFile, "r") as dataFile:
        data = json.loads(dataFile.read())

        return data["message"], data["commands"]

dataMessage, dataCommands = readDataFile(settings.FACEBOOK["BOT_DATA_FILE"])

fb = FacebookConstructor(
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=dataMessage,
    commands=dataCommands,
    shopData=settings.SHOPS,
    resultItemCount=settings.FACEBOOK["RESULT_ITEMS_COUNT"],
)

@app.route("/", methods=['GET'])
def verify():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == settings.FACEBOOK["VERIFY_TOKEN"]:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

@app.route("/", methods=['POST'])
def webhook():
    """
    1) select command - all message or post COMMAND
    2) select store - SHOP
        2.1) Select simple top list - TOP
        2.2) Select list with discount - DISCOUNT
            2.2.1) User select discout
    3) select caliber from current shop
    4) Print top list
    """
    data = request.get_json()
    recipient_id, message = fb.getMessage(data)

    if recipient_id and message:
        dataCategory = ''

        """ Test if it post data """
        if message.find("__") != -1:
            dataCategory = message.split("__")[0]
            dataId = message.split("__")[1]

        if dataCategory == "SHOP": # (2)
            if dataId == "DISCOUNT": # (2.2.1)
                bot.send_generic_message(
                    recipient_id,
                    fb.printListDiscount()
                )
            else: # (2.1)
                bot.send_generic_message(
                    recipient_id,
                    fb.botSelectStore()
                )
        elif dataCategory == "DISCOUNT":  # (2.2)
            fb.setDiscount(dataId)
            bot.send_generic_message(
                recipient_id,
                fb.botSelectStore()
            )
        elif dataCategory == "CHOICE": # (3)
            bot.send_generic_message(
                recipient_id,
                fb.botCaliberChoice()
            )
        elif dataCategory == "TOP": # (4)
            textArray, link = fb.botPrintTop(dataId)
            textFormated = fb.separateText(textArray)

            if len(textFormated) >= 640: # test message for chars limit - for facebook it's 640 chars
                textPartFirst, textPartSecond = fb.separateMesageToTwo(textArray)

                bot.send_text_message(
                    recipient_id,
                    textPartFirst
                )
                textFormated = textPartSecond
                    
            bot.send_button_message(
                recipient_id,
                textFormated,
                fb.createButtonLink(
                    dataMessage["link_text"],
                    link
                )
            )
        else: # (1)
            bot.send_button_message(
                recipient_id,
                dataMessage["select_commad"],
                fb.botCommands()
            )
    
    return "ok", 200


@app.route("/privacy-policy.html")
def show_privacyPolicy():
    return render_template('privacy-policy.html')

if __name__ == "__main__":
    app.run(port=settings.FACEBOOK["PORT"], debug=True)
