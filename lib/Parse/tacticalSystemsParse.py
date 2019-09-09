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
        price = re.sub('[^0-9a-zA-Z]+', '.', price[0])
        price = price[:-1]

        try:
            return float(price)
        except ValueError:
            price = price.replace('.', '', 2)
            price = float(price[:-2])

            return price

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="catalogCard-main"]')

        for item in blocks:
            price = item.xpath('.//div[@class="catalogCard-price"]/text()')

            if price:
                dic = {}
                name = item.xpath('.//div[@class="catalogCard-title"]/a/text()')

                dic["title"] = self.cleanTitle(name[0])
                dic["price"] = self.cleanPriceNum(price)

                result.append(dict(dic))
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
    