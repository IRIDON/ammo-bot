# -*- coding: utf-8 -*-
import json, os
from config import settings
from flask import Flask, request, send_from_directory
from lib.Constructor.facebookConstructor import FacebookConstructor, BotSetSettings
from lib.Web.page import Page

app = Flask(__name__)
viewPage = Page(settings.WEB)
fb = FacebookConstructor(
    token=settings.FACEBOOK["ACCESS_TOKEN"],
    dataFile=settings.FACEBOOK["BOT_DATA_FILE"],
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    shopData=settings.SHOPS,
    resultItemCount=settings.FACEBOOK["RESULT_ITEMS_COUNT"],
)
botSettings = BotSetSettings(
    token=settings.FACEBOOK["ACCESS_TOKEN"],
    dataFile=settings.FACEBOOK["BOT_DATA_FILE"],
    shopData=settings.SHOPS
)

botSettings.getStart()
botSettings.setMenu()

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == settings.FACEBOOK["VERIFY_TOKEN"]:
            return request.args.get("hub.challenge")
        else:
            return viewPage.page("home")

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
                fb.printListDiscount(recipient_id)
            else: # (2.1)
                fb.setDiscount("0%")
                fb.botSelectStore(recipient_id)
        elif dataCategory == "DISCOUNT": # (2.2)
            fb.setDiscount(dataId)
            fb.botSelectStore(recipient_id)
        elif dataCategory == "CHOICE": # (3)
            fb.botCaliberChoice(recipient_id)
        elif dataCategory == "TOP": # (4)
            fb.botPrintTop(dataId , recipient_id)
        elif dataCategory == "COMMANDS": # (4)
            fb.botCommands(recipient_id)
        else: # (1)
            fb.botNone(recipient_id)
    
    return "ok", 200

@app.route("/<page>")
def page(page):
    page = page.replace(".html", "")

    return viewPage.page(page)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.errorhandler(404)
def page_not_found(error):
    return viewPage.page("error")

if __name__ == "__main__":
    app.run(port=settings.FACEBOOK["PORT"], debug=True)
