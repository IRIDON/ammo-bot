# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

class ShopGunData(ParseData):
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
        price = re.sub('[^0-9a-zA-Z-.]+', '', price)

        return float(price)

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath("//div[contains(@class, 'product-layoutcat')]") 

        for item in blocks:
            dic = {}
            name = item.xpath('.//h4/a/text()')
            price = item.xpath('.//p[@class="price"]/text()')

            if price:
                name = name[0].replace('\n', '')
                print(name)
                calcPrice = self.cleanPriceNum(price[0]);

                dic["title"] = name
                dic["price"] = round(calcPrice, 2)

                result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    