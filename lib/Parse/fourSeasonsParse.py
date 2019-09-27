# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
import re

class FourSeasonsParseData(ParseData):
    __slots__ = [
        "categories",
        "availableAmmo",
        "url",
        "urlTmp",
        "dataFile",
        "shopName"
    ]
    def __init__(self):
        settings = shops["four_seasons"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanTitle(self, title):
        title = title.replace(u"Патрон нарізний ", "")
        title = title.replace(u"Патрон ", "")
        title = title.replace(u"Набій ", "")

        return title

    def getRequestProp(self, urlTmp):
        requestData = {
            "order": 2,
            "limit": 100,
            "orderby": 0
        }
        url, key = urlTmp.split('---')

        if key and key != '0':
            requestData["extra_fields[19][]"] = key

        return url, requestData

    def getStructure(self, urlTmp):
        result = []
        url, requestData = self.getRequestProp(urlTmp)
        page = self.requestsPostPage(url, requestData)

        blocks = page.xpath('//div[@class="span4 block_product"]')

        for item in blocks:
            dic = {}
            nameBlock = item.xpath('.//div[@class="name"]/a/text()')
            priceBlock = item.xpath('.//div[@class="jshop_price"]/span/text()')

            if priceBlock and nameBlock:
                name = nameBlock[0]
                price = self.cleanPriceNum(priceBlock[0])

                dic["title"] = self.cleanTitle(name)
                dic["price"] = price

                result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    