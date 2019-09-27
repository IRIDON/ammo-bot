# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
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
    def __init__(self):
        settings = shops["shopgun"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath("//div[contains(@class, 'product-layoutcat')]") 

        for item in blocks:
            dic = {}
            nameBlock = item.xpath('.//h4/a/text()')
            priceBlock = item.xpath('.//p[@class="price"]/text()')

            if priceBlock:
                price = priceBlock[0]
                name = nameBlock[0].replace('\n', '')
                calcPrice = self.cleanPriceNum(price);

                dic["title"] = self.cleanTitle(name)
                dic["price"] = round(calcPrice, 2)

                result.append(
                    dict(dic)
                )

        return sorted(result, key=self.sortArrayByPrice)
    