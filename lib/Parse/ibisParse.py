# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

class IbisParseData(ParseData):
    __slots__ = [
        "ammo_type",
        "dataFile",
        "availableAmmo",
        "urlTmp",
        "shopName"
    ]
    def __init__(self, settings):
        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.dataFile = settings["data_file"]
        self.availableAmmo = settings["category"]
        self.urlTmp = settings["url_tmp"]

    def getPrices(self, tree):
        priceBlock = tree.xpath('.//div[contains(@class, "pb_price")]')
        price = priceBlock[0]
        priceText = price.xpath('./text()')

        if len(priceText[0].strip()):
            return float(priceText[0])
        else:
            pn = price.xpath('*/text()')

            return float(pn[0] + pn[1])

    def getStructure(self, url):
        result = []
        amountCategory = self.availableAmmo['22_LR'][0]
        page = self.requestsPage(url)
        blocks = page.xpath('.//form[@class="product_brief_list "]')

        for item in blocks:
            price = self.getPrices(item)

            if price:
                dic = {}
                nameBlock = item.xpath('.//a[@class="pb_product_name"]/text()')
                name = nameBlock[0]

                if(amountCategory in url):
                    extra = item.xpath('.//div[@class="pb_extra"]/text()')
                    extraStr = ','.join(extra)
                    amount = self.getAmount(extraStr)
                    price = self.getPriceByAmount(price, amount)

                dic["title"] = self.cleanTitle(name).encode('utf-8').strip()
                dic["price"] = price

                result.append(dict(dic))
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
