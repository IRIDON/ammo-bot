# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

class KulyaParseData(ParseData):
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
        price = price.split(" ")[0]
        price = re.sub('[^0-9a-zA-Z]+', '.', price)

        if price[len(price) - 1] == '.':
            price = price[:-1]

        return float(price)

    def getAmount(self, string):
        amount = 1;
        amountRe = re.search("\(([0-9]+)?%s\)" % (u"шт"), string)

        if amountRe:
            amount = int(amountRe.group(1));

        return amount

    def getPriceByAmount(self, price, amount):
        calcPrice = round(price / amount, 2)

        if (calcPrice < 1):
            calcPrice = price

        price = calcPrice

        return price

    def getStructure(self, url):
        result = []
        page = self.requestsUrllib2Page(url)
        blocks = page.xpath('//div[@class="product-thumb"]')

        for item in blocks:
            dic = {}
            nameBlock = item.xpath('.//div[@class="product-name"]/a/text()')
            priceBlock = item.xpath('.//p[@class="price"]/span/text()')

            if priceBlock and nameBlock:
                name = nameBlock[0]
                price = self.cleanPriceNum(priceBlock[0])
                amount = self.getAmount(name);
                price = self.getPriceByAmount(price, amount)

                dic["title"] = name
                dic["price"] = price

                result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    