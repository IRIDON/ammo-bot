# -*- coding: utf-8 -*-
import json, requests
from lib.Constructor.botConstructor import BotConstructor
from pymessenger.bot import Bot

import logging

logging.basicConfig(
    format = u'%(levelname)-8s [%(asctime)s] %(message)s',
    level = logging.ERROR,
    filename = u'log/log.log'
)

log = logging

log.critical("Init app")

DEFAULT_API_VERSION = 2.6

class FacebookConstructor(BotConstructor):
    __slots__ = [
        "accessToken",
        "bot",
        "currency",
        "availableDiscount",
        "message",
        "commands",
        "shopData",
        "visibleTopItems",
        "availableShops",
        "currentShop",
        "categories",
        "categoriesKeys",
        "availableAmmo",
        "dataFileUrl",
        "discount"
    ]
    def __init__(self, **kwargs):
        self.accessToken = kwargs["token"]
        self.bot = Bot(self.accessToken)
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.shopData = kwargs["shopData"]
        self.visibleTopItems = kwargs["resultItemCount"]
        self.availableShops = self.shopData.keys()
        self.currentShop = self.availableShops[0]
        self.discount = 0
        self.readDataFile(kwargs["dataFile"])
        self.initShopData(self.currentShop)

    """ Parse facebook data and return message """
    def getMessage(self, data):
        try:
            for event in data['entry']:
                for item in event['messaging']:
                    recipient_id = item['sender']['id']

                    if item.get('message'):
                        message = item['message']

                        if message.get('quick_reply'):
                            message_text = message['quick_reply']['payload']
                        elif message.get('text') and not message.get('app_id'):
                            message_text = message['text']
                        else:
                            return False, False

                    elif item.get('postback'):
                        message_text = item['postback']['payload']
                    else:
                        return False, False

                    return recipient_id, message_text
                    
        except Exception as error:
            log.error(error)

    def readDataFile(self, dataFile):
        with open(dataFile, "r") as dataFile:
            data = json.loads(dataFile.read())

            self.message = data["message"]
            self.commands = data["commands"]

    """ find and structure offer results for choise shop and caliber """
    def topPrices(self, num=3, category='', discount=0):
        result = []
        allData = self.getData()

        if not allData:
            return self.message["base_error"]

        data = allData[category]
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        for index in range(0,num):
            title = data[index]["title"]
            price = data[index]["price"]

            if discount == 0:
                result.append("%s %s - %s" % (price, self.currency, title))
            else:
                result.append("%s %s \"%s\" - %s" % (
                    self.getDiscount(price, discount),
                    self.currency,
                    price,
                    title
                ))
        
        result.append(allData["url"][category])
        
        return result

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def separateText(self, text):
        return "\n\n".join(text)

    def separateMesageToTwo(self, textArray):
        lenArr = len(textArray) / 2
        first = self.separateText(textArray[:lenArr])
        second = self.separateText(textArray[lenArr:])

        return first, second

    def getAllShopsNames(self, shopData):
        result = []

        for shopName in shopData:
            shop = shopData[shopName]
            
            result.append(shop["shop_name"])

        return ", ".join(result)

    def setDiscount(self, discount):
        try:
            discount = discount.replace("%", "")
            discount = int(discount)

            self.discount = discount
        except Exception as error:
            log.error(error)
        
    """ Create slide button group """
    def createButtonGroup(self, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s__%s" % (dataId.upper(), name)

            result.append(dic)
        
        return list(self.chunks(result, 3))

    """ Create button pack for button group """
    def botCreateButtons(self, title, arr, dataId):
        result = []
        buttons = self.createButtonGroup(arr, dataId)

        for item in buttons:
            dic = {}
            dic["title"] = title
            dic["buttons"] = item

            result.append(dic)

        return result

    def botCreadeQuickReplies(self, text, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["content_type"] = "text"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s__%s" % (dataId.upper(), name)

            result.append(dic)

        return {
            "text": text,
            "quick_replies": result
        }

    """ Create button link """
    def createButtonLink(self, title, link):
        result = []

        dic = {}
        dic["type"] = "web_url"
        dic["title"] = title
        dic["url"] = link

        result.append(dic)
        
        return result

    """ Create structure for list main commans """
    def getFormateCommands(self, data):
        result = []
  
        for key in data:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = data[key][1]
            dic["payload"] = "%s__%s" % (data[key][0], key.upper())

            result.append(dic)

        return result

    def botCommands(self, recipient_id):
        try:
            self.bot.send_button_message(
                recipient_id,
                self.message["select_commad"],
                self.getFormateCommands(self.commands)
            )
        except Exception as error:
            log.error(error)

    def botNone(self, recipient_id):
        try:
            self.bot.send_text_message(
                recipient_id,
                self.message["no_commad"][0],
            )
        except Exception as error:
            log.error(error)

    """ Print aviable discounts """
    def printListDiscount(self, recipient_id):
        try:
            doscounts = []

            for item in self.availableDiscount:
                doscounts.append(
                    str(item) + "%"
                )
                
            keyboard = self.botCreadeQuickReplies(
                self.message["select_discount"],
                doscounts,
                "discount"
            )

            self.bot.send_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error(error)

    """ Print aviable shops list """
    def botSelectStore(self, recipient_id):
        try:
            shopName = []

            for shop in self.availableShops:
                shopName.append(shop.upper())
                
            keyboard = self.botCreadeQuickReplies(
                self.message["select_store"],
                shopName,
                "choice"
            )

            self.bot.send_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error(error)

    """ Print aviable caliber list for current shop """
    def botCaliberChoice(self, recipient_id):
        try:
            keyboard = self.botCreateButtons(
                self.message["select_caliber"],
                self.categoriesKeys,
                "top"
            )
            self.bot.send_generic_message(
                recipient_id,
                keyboard
            )
        except Exception as error:
            log.error(error)

    """ Print offers """
    def botPrintTop(self, currentCaliber, recipient_id):
        try:
            text = self.topPrices(
                self.visibleTopItems,
                str(currentCaliber),
                self.discount
            )
            textArray = text[:-1]
            link = text[-1]
            textFormated = self.separateText(textArray)

            if len(textFormated) >= 640: # test message for chars limit - for facebook it's 640 chars
                textPartFirst, textPartSecond = self.separateMesageToTwo(textArray)

                self.bot.send_text_message(
                    recipient_id,
                    textPartFirst
                )
                textFormated = textPartSecond
                    
            self.bot.send_button_message(
                recipient_id,
                textFormated,
                self.createButtonLink(
                    self.message["link_text"],
                    link
                )
            )
        except Exception as error:
            log.error(error)

class BotSetSettings(FacebookConstructor):
    __slots__ = {
        "url",
        "accessToken",
        "shopData",
        "message",
        "commands"
    }
    def __init__(self, token, dataFile, shopData):
        self.url = "https://graph.facebook.com/v%s/me/messenger_profile?access_token=%s"
        self.accessToken = token
        self.shopData = shopData
        self.readDataFile(dataFile)
        
    def getStart(self):
        textResult = []
        textData = self.message["greeting_text"]
        command = "COMMANDS__COMMANDS"

        for key, value in textData.iteritems():
            textResult.append({
                "locale": key,
                "text": value  % (self.getAllShopsNames(self.shopData))
            })

        payload = {
            "setting_type": "greeting",
            "greeting": textResult,
            "get_started": {
                "payload": command
            }
        }

        return self.botSendProfile(payload)

    def setMenu(self):
        payload = {
            "persistent_menu": [
                {
                    "locale": "default",
                    "composer_input_disabled": True,
                    "call_to_actions": self.getFormateCommands(self.commands)
                }
            ]
        }

        return self.botSendProfile(payload)

    def botSendProfile(self, payload):
        request_endpoint = self.url % (DEFAULT_API_VERSION, self.accessToken)
        response = requests.post(
            request_endpoint,
            json=payload
        )

        return response.json()
