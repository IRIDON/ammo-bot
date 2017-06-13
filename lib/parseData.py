# -*- coding: utf-8 -*-

"""
Parse data from websile ibis.net.ua
create JSON data and save it in file
"""

from config import default_settings as settings
from lxml import html
import requests
import json
import time

def getKey(item):
    return item["price"]

class IbisParseData(object):
    def __init__(self):
        self.categories = settings["CALIBERS"]
        self.dataFileUrl = settings["DATA_FILE"]
        self.availableAmmo = settings["AMMO_TYPE"]
        self.urlTmp = settings["URL_TMP"]

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

        return self.urlTmp % (self.availableAmmo[category[1]], category[0])

    def parse(self):
        try:
            data = {}

            for categoryName in self.categories.keys():
                url = self.getUrl(categoryName)
                data[categoryName] = self.getData(url)

            data["time"] = self.getCurrentTime()
            self.saveData(json.dumps(data))
        except Exception as e:
            print e
        finally:
            print "Parse successful"

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

    def getCurrentTime(self):
        timetup = time.gmtime(time.time() + 3 * 60 * 60)
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', timetup)

        return currentTime
