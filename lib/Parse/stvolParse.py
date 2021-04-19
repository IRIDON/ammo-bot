# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
import re

class StvolParseData(ParseData):
    __slots__ = [
        "categories",
        "availableAmmo",
        "url",
        "urlTmp",
        "dataFile",
        "shopName"
    ]
    def __init__(self):
        settings = shops["stvol"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def _findAmount(self, items):
        for text in items:
            amount = self.getAmount(text)

            if amount > 1:
                return amount
        else:
            return 1

    def _getAmount(self, item):
        amountTexts = item.xpath('.//div[@class="tov-option-line"]/text()')
        amount = self._findAmount(amountTexts)

        if amount > 1:
            return amount
        else:
            url = item.xpath('.//a[@class="tov-name"]/@href')
            amount_url = self._getAmountFromUrl(url[0])

            if amount_url > 1:
                return amount_url
            else:
                return amount

    def _getAmountFromUrl(self, url):
        page = self.requestsPage(self.url + url)
        blocks = page.xpath('.//*[@class="characteristics-line"]/text()')
        amount = self._findAmount(blocks)

        return amount

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="cover-tov"]')

        for item in blocks:
            dic = {}
            nameBlock = item.xpath('.//a[@class="tov-name"]/text()')
            price_1 = item.xpath('.//div[@class="current-price"]/b/text()')[0].replace(' ', '')
            price_2 = item.xpath('.//div[@class="current-price"]/text()')[0]
            avilible = item.xpath('.//div[@class="no-item"]')

            if len(avilible) == 0:
                amount = 1
                price = self.cleanPriceNum(price_1 + price_2) 
                name = nameBlock[0]
                amountCategory = self.availableAmmo['22_LR'][0];

                if(amountCategory in url):
                    amount = self._getAmount(item)

                dic["title"] = self.cleanTitle(name)
                dic["price"] = self.getPriceByAmount(price, amount)

                result.append(
                    dict(dic)
                )

        return sorted(result, key=self.sortArrayByPrice)
    