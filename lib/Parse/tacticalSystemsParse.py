# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
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
    def __init__(self):
        settings = shops["tactical-systems"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanName(self, name):
        return name.replace('\n', '').strip();

    def getStructure(self, url):
        result = []
        amountCategory = self.availableAmmo['22_LR'][0]
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="catalogCard-main"]')

        for item in blocks:
            priceBlock = item.xpath('.//div[@class="catalogCard-price"]/text()')
            nameBlock = item.xpath('.//div[@class="catalogCard-title"]/a/text()')

            if priceBlock and nameBlock:
                dic = {}
                name = self.cleanName(nameBlock[0])
                price = self.cleanPriceNum(
                    priceBlock[0].replace(' ', '')
                )

                if(amountCategory in url):
                    amount = self.getAmount(name)
                    price = self.getPriceByAmount(price, amount)

                dic["title"] = self.cleanTitle(name)
                dic["price"] = price

                result.append(
                    dict(dic)
                )
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
    