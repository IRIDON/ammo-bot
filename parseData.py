# -*- coding: utf-8 -*-
from __init__ import *
from lxml import html
import requests
import json

def getKey(item):
    return item["price"]

class IbisParseData(object):
    def __init__(self):
        self.categories = CALIBERS
        self.dataFileUrl = DATA_FILE

    def coder(self, text):
        return text.encode('utf-8')

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

    def getStructure(self, tree, price):
        title = tree.xpath('//a[@class="pb_product_name"]/text()')
        stock = tree.xpath('//div[@class="pb_stock"]')
        result = []

        for index, item in enumerate(price):
            dic = {}
            dic["title"] = self.coder(title[index])
            dic["price"] = float(price[index])

            if not stock[index].xpath('*/text()'):
                result.append(dict(dic))
            else:
                break

        return result

    def getUrl(self, categoryName):
        category = self.categories[categoryName]

        return URL_TMP % (AMMO_TYPE[category[1]], category[0])

    def parse(self):
        data = {}

        for categoryName in self.categories.keys():
            url = self.getUrl(categoryName)
            data[categoryName] = self.getData(url)

        self.saveData(json.dumps(data))

    def getData(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        price = self.getPrices(tree)
        data = self.getStructure(tree, price)

        return data

    def saveData(self, dataJson):
        with open(self.dataFileUrl, "w") as file:
            file.truncate() #clean file data
            file.write(str(dataJson))

ibisParseData = IbisParseData()
ibisParseData.parse()