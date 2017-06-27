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
                    message = item['message']['text']
                elif item.get('postback'):
                    message = item['postback']['payload']
                else:
                    return False

                return recipient_id, message

    def chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def botCreateButtons(self, arr, dataId):
        result = []

        for name in arr:
            dic = {}
            dic["type"] = "postback"
            dic["title"] = self.getKeyName(name)
            dic["payload"] = "%s-%s" % (dataId.upper(), name.upper())

            result.append(dic)
        
        return list(self.chunks(result, 3))
    
    def botSelectStore(self):
        shopName = []

        for shop in self.availableShops:
            shopName.append(shop.upper())
            
        return self.botCreateButtons(shopName, 'shop')

    def botInitTop(self, message):
        try:
            self.discount = 0
            recipient_id, message = self.getMessage(message)
            keyboard = self.botCreateButtons(self.categoriesKeys, 'top')

            self.botSendMessage(
                recipient_id,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper()),
                keyboard,
            )
        except Exception as error:
            print error

    # def botInitDiscount(self, message):
    #     try:
    #         recipient_id, message = self.getMessage(message)
    #         keyboard = self.botCreateButtons(self.availableDiscount, 'discount')

    #         self.botSendMessage(
    #             recipient_id,
    #             self.message["choose_discount"],
    #             keyboard
    #         )
    #     except Exception as error:
    #         print error

    def botPrintTop(self, callData):
        try:
            recipient_id, message = self.getMessage(message)
            data = message.split("-")
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = self.topPrices(
                self.visibleTopItems,
                currentCaliber,
                self.discount
            )

            self.botSendMessage(recipient_id, result)
        except Exception as error:
            print error
