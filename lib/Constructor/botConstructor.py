# -*- coding: utf-8 -*-
import json

class BotConstructor(object):
    __slots__ = [
        "currency",
        "message",
        "shopData"
    ]
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]

    def initShopData(self, shopName):
        shopName = shopName.lower()
        
        if self.shopData[shopName]:
            shopData = self.shopData[shopName]

            self.categories = shopData["category"]
            self.categoriesKeys = self.categories.keys()
            self.availableAmmo = shopData["ammo_type"]
            self.dataFileUrl = shopData["data_file"]
            self.currentShop = shopName
        else:
            return False

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return format(price * factor, '.2f')

    def topPrices(self, num=3, category='', discount=0):
        result = []
        allData = self.getData()

        if not allData:
            return self.message["base_error"]

        data = allData[category]
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        result.append("<b>%s</b>\n" % (self.getKeyName(category)))

        for index in range(0,num):
            title = data[index]["title"]
            price = data[index]["price"]

            if discount == 0:
                result.append("<b>%s %s</b> - %s" % (price, self.currency, title))
            else:
                result.append("<b>%s %s</b> <i>(%s)</i> - %s" % (
                    self.getDiscount(price, discount),
                    self.currency,
                    price,
                    title)
                )
        
        result.append("\n<i>%s: %s</i>" % (
            self.message["base_date"],
            allData["time"]
        ))
        result.append("\n<a href='%s'>%s</a>" % (
            allData["url"][category] + "?utm_source=ammoBot",
            self.message["link_text"]
        ))
        
        return "\n".join(result)

    def getKeyName(self, name):
        return name.replace("_", " ")

    def toSeconds(self, day):
        return day * 24 * 60 * 60

    def capitalize(self, text):
        return text[:1].upper() + text[1:]
    