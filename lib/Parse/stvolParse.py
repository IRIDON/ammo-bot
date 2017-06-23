# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

class StvolParseData(ParseData):
    __slots__ = ["categories", "availableAmmo", "url", "urlTmp", "dataFile", "shopName"]
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

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="tov-cover"]')

        for item in blocks:
            dic = {}
            name = item.xpath('.//div[@class="tov-name"]/a/text()')
            price_1 = item.xpath('.//div[@class="price"]/b/text()')[0].replace(' ', '')
            price_2 = item.xpath('.//div[@class="price"]/text()')[0]

            dic["title"] = name[0]
            dic["price"] = self.cleanPriceNum(price_1 + price_2) 

            result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    