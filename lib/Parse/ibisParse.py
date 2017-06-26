# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html

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
        price = tree.xpath('//div[@class="pb_price "]')
        result = []

        for item in price:
            pr = item.xpath('./text()')

            if pr:
                result.append(float(pr[0]))
            else:
                pn = item.xpath('*/text()')

                result.append(float(pn[0] + pn[1]))

        return result

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        price = self.getPrices(page)
        title = page.xpath('//a[@class="pb_product_name"]/text()')
        stock = page.xpath('//div[@class="pb_stock"]')
        
        for index, item in enumerate(price):
            dic = {}
            dic["title"] = self.coder(title[index])
            dic["price"] = float(price[index])
            
            if not stock[index].xpath('*/text()'):
                result.append(dict(dic))
            else:
                break

        return result
