# -*- coding: utf-8 -*-

from lib.parseData import ParseData
from lxml import html
import requests
import json
import re

class SafariParseData(ParseData):
    __slots__ = ["categories", "ammo", "availableAmmo", "url", "urlTmp", "dataFile", "shopName"]
    def __init__(self, settings):
        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.ammo = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def sortArrayByPrice(self, x):
        return x["price"]

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="g-l-i g-l-i-list"]')

        for item in blocks:
            price = item.xpath('.//div[@name="price"]/text()')
            
            if price:
                dic = {}
                name = item.xpath('.//a[@class="g-l-i-details-title-link"]/text()')
                price = re.sub('[^0-9a-zA-Z]+', '.', price[0])
                price = price[:-1]

                dic["title"] = name[0]
                dic["price"] = float(price)

                result.append(dict(dic))
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)

    def getUrl(self, id):
        category = self.availableAmmo[id][1]
        key = self.availableAmmo[id][0]
        part = self.categories[category]

        return self.urlTmp % (part, key)

    def parse(self):
        try:
            result = {
                "url": {}
            }
            
            for ammo in self.availableAmmo:
                url = self.getUrl(ammo)
                data = self.getStructure(url)

                result[ammo] = data
                result["url"][ammo] = url

            result["time"] = self.getCurrentTime()

            self.saveData(self.dataFile, json.dumps(result))
        except Exception as e:
            print e
        finally:
            print "Parse %s successful" % (self.shopName)
    