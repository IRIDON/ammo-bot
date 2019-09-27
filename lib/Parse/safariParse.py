# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
import re

class SafariParseData(ParseData):
    __slots__ = [
        "categories",
        "availableAmmo",
        "url",
        "urlTmp",
        "dataFile",
        "shopName"
    ]
    def __init__(self):
        settings = shops["safari"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="g-l-i g-l-i-list"]')

        for item in blocks:
            priceBlock = item.xpath('.//div[@name="price"]/text()')

            if priceBlock:
                dic = {}
                nameBlock = item.xpath('.//div[@class="g-l-i-details-title"]/a/text()')
                price = priceBlock[0]
                name = nameBlock[0]

                dic["title"] = self.cleanTitle(name).encode('raw-unicode-escape')
                dic["price"] = self.cleanPriceNum(price)

                result.append(
                    dict(dic)
                )
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
    