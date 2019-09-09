# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

class TacticalSystemsParseData(ParseData):
    __slots__ = [
        "categories",
        "availableAmmo",
        "url",
        "urlTmp",
        "dataFile",
        "shopName"
    ]
    def __init__(self, settings):
        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanPriceNum(self, price):
        price = re.sub('[^0-9a-zA-Z]+', '.', price)
        price = price[:-1]

        try:
            return float(price)
        except ValueError:
            price = price.replace('.', '', 2)
            price = float(price[:-2])

            return price

    def getAmount(self, str):
        amount = 1
        amountRe = re.search("([0-9]+) ?%s" % (u"шт"), str)

        if amountRe:
            amount = int(amountRe.group(1))

        return amount

    def getPriceByAmoint(self, price, amount):
        calcPrice = round(price / amount, 2)

        if (calcPrice < 1):
            calcPrice = price

        price = calcPrice

        return price

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="catalogCard-main"]')

        for item in blocks:
            priceBlock = item.xpath('.//div[@class="catalogCard-price"]/text()')

            if priceBlock:
                dic = {}
                price = self.cleanPriceNum(priceBlock[0])
                name = item.xpath('.//div[@class="catalogCard-title"]/a/text()')
                amount = self.getAmount(name[0])

                dic["title"] = self.cleanTitle(name[0])
                dic["price"] = self.getPriceByAmoint(price, amount)

                result.append(dict(dic))
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
    