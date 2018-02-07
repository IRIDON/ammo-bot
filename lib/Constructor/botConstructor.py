# -*- coding: utf-8 -*-
import json
import statistics

class BotConstructor(object):
    __slots__ = [
        "currency",
        "message",
        "shopData",
        "dataUpdateTime"
    ]
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.dataUpdateTime = ''

    def initShopData(self, shopName):
        if self.shopData[shopName]:
            shopData = self.shopData[shopName]

            self.categories = sorted(shopData["category"].items(), key=lambda item: item[1][2])
            self.categoriesKeys = map(lambda x: x[0], self.categories)
            self.availableAmmo = shopData["ammo_type"]
            self.dataFileUrl = shopData["data_file"]
        else:
            return False

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return format(price * factor, '.2f')

    def chunkArr(self, seq, num):
        num = len(seq) / num
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out

    def topPrices(self, num=3, category='', discount=0):
        allData = self.getData()

        if not allData:
            return self.message["base_error"]

        self.dataUpdateTime = allData["time"]

        result = self.formateResult(
            allData[category],
            num,
            category,
            discount
        )

        result.append("\n<a href='%s'>%s</a>" % (
            allData["url"][category] + "?utm_source=ammoBot",
            self.message["link_text"]
        ))

        return "\n".join(result)

    def allShopPrices(self, category, num=10):
        result = self.allPrices(category, num)

        return "\n".join(result)

    def formateResult(self, data, num=3, category='', discount=0):
        result = []
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        result.append("<b>%s</b>\n" % (self.getKeyName(category)))

        for index in range(0, num):
            item = data[index]
            shopName = item.get('shop_name')
            title = item["title"]
            price = item["price"]
            template = "<b>%s %s</b> - %s"
            resultArr = [price, self.currency, title]

            if discount != 0 and not shopName:
                template = "<b>%s %s</b> <i>(%s)</i> - %s"
                resultArr = (
                    self.getDiscount(price, discount),
                    self.currency,
                    price,
                    title
                )
            elif shopName:
                template = "<b>%s %s</b> - %s (%s)"
                resultArr.append(shopName)

            result.append(template % tuple(resultArr))

        if len(result) == 1:
            result.append(self.message["no_results"])

        if self.dataUpdateTime:
            result.append("\n<i>%s: %s</i>" % (
                self.message["base_date"],
                self.dataUpdateTime
            ))

        return result

    def allPrices(self, caliber, num):
        data = self.shopData
        result = []
        dataFiles = []

        for shopName in self.shopData:
            shop = data[shopName]

            with open(shop["data_file"], "r") as file:
                f = json.load(file)

                if not self.dataUpdateTime:
                    self.dataUpdateTime = f['time']

                if caliber in f:
                    for item in f[caliber]:
                        item['shop_name'] = shop['shop_name'].upper()

                        dataFiles.append(item)

        data = sorted(dataFiles, key=lambda x: x["price"])

        return self.formateResult(
            data,
            num,
            caliber
        )

    def getKeyName(self, name):
        return name.replace("_", " ")

    def toSeconds(day):
        return day * 24 * 60 * 60
    