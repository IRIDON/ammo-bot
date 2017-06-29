# -*- coding: utf-8 -*-
import json
from lib.Constructor.botConstructor import BotConstructor

class FacebookConstructor(BotConstructor):
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.message = kwargs["message"]
        self.commands = kwargs["commands"]
        self.shopData = kwargs["shopData"]
        self.visibleTopItems = kwargs["resultItemCount"]
        self.availableShops = self.shopData.keys()
        self.currentShop = self.availableShops[0]
        self.discount = 0
        self.initShopData(self.currentShop)

    """ Parse facebook data and return message """
    def getMessage(self, data):
        for event in data['entry']:

            for item in event['messaging']:
                recipient_id = item['sender']['id']

                if item.get('message'):
                    message = item['message']

                    if message.get('text'):
                        message = message['text']
                    else:
                        return False, False

                elif item.get('postback'):
                    message = item['postback']['payload']
                else:
                    return False, False

                return recipient_id, message

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
                result.append("%s %s(%s) - %s" % (
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

    def setDiscount(self, discount):
        try:
            discount = discount.replace("%", "")
            discount = int(discount)

            self.discount = discount
        except Exception as e:
            raise
        
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
    def botCommands(self):
        result = []
        data = self.commands
        self.discount = 0

        for key in data:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = data[key][1]
            dic["payload"] = "%s__%s" % (data[key][0], key.upper())

            result.append(dic)

        return result

    """ Print aviable discounts """
    def printListDiscount(self):
        doscounts = []

        for item in self.availableDiscount:
            doscounts.append(
                str(item) + "%"
            )
            
        return self.botCreateButtons(
            self.message["select_discount"],
            doscounts,
            "discount"
        )

    """ Print aviable shops list """
    def botSelectStore(self):
        shopName = []

        for shop in self.availableShops:
            shopName.append(shop.upper())
            
        return self.botCreateButtons(
            self.message["select_store"],
            shopName,
            "choice"
        )

    """ Print aviable caliber list for current shop """
    def botCaliberChoice(self):
        return self.botCreateButtons(
            self.message["select_caliber"],
            self.categoriesKeys,
            "top"
        )

    """ Print offers """
    def botPrintTop(self, currentCaliber):
        text = self.topPrices(
            self.visibleTopItems,
            str(currentCaliber),
            self.discount
        )

        return text[:-1], text[-1]
