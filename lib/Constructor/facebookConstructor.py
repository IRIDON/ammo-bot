# -*- coding: utf-8 -*-
import json
from lib.Constructor.botConstructor import BotConstructor

class FacebookConstructor(BotConstructor):
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.visibleTopItems = kwargs["resultItemCount"]
        self.availableShops = self.shopData.keys()
        self.currentShop = self.availableShops[0]
        self.discount = 0
        self.initShopData(self.currentShop)

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

    def botCreateButtons(self, title, arr, dataId):
        result = []
        buttons = self.createButtonGroup(arr, dataId)

        for item in buttons:
            dic = {}
            dic["title"] = title
            dic["buttons"] = item

            result.append(dic)

        return result

    def createButtonGroup(self, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s__%s" % (dataId.upper(), name)

            result.append(dic)
        
        return list(self.chunks(result, 3))
    
    def botSelectStore(self):
        shopName = []

        for shop in self.availableShops:
            shopName.append(shop.upper())
            
        return self.botCreateButtons(
            "Swipe left/right for more options.",
            shopName,
            "shop"
        )

    def botInitTop(self):
        self.discount = 0

        return self.botCreateButtons(
            "Swipe left/right for more options.",
            self.categoriesKeys,
            "top"
        )

    def botPrintTop(self, currentCaliber):
        text = self.topPrices(
            self.visibleTopItems,
            str(currentCaliber),
            self.discount
        )

        return "\n".join(text[:-1]), text[-1]
