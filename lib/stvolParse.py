# -*- coding: utf-8 -*-

from lib.parseData import ParseData
from lxml import html
import requests
import json
import re

class StvolParseData(ParseData):
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

    def getCategoryUrl(self, category):
        result = {}
        url = self.urlTmp % (category)
        page = requests.get(url)
        tree = html.fromstring(page.content)
        filterBlocks = tree.xpath('//div[@class="side-block active"]')
        block = {}

        for item in filterBlocks:
            value = item.xpath('.//input//@name')[0]

            if value.find("_502_") != -1:
                block = item
                break

        links = block.xpath('.//a//@href')
        calibersName = block.xpath('.//a//text()')

        for index, link in enumerate(links):
            name = calibersName[index].replace(" ", "_")
            result[name] = self.url + link + "?per_page=96"

        return result

    def getCategory(self):
        result = {}

        for category in self.categories:
            categoryUrl = self.getCategoryUrl(category)
            result.update(categoryUrl)

        return result

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="tov-cover"]')

        for item in blocks:
            dic = {}
            name = item.xpath('.//div[@class="tov-name"]/a/text()')
            price_1 = item.xpath('.//div[@class="price"]/b/text()')[0].replace(' ', '')
            price_2 = item.xpath('.//div[@class="price"]/text()')[0]
            price = price_1 + price_2
            price = price.split(" ")[0]
            price = re.sub('[^0-9a-zA-Z]+', '.', price)

            if price[len(price) - 1] == '.':
                price = price[:-1]

            dic["title"] = name[0]
            dic["price"] = float(price)

            result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)

    def parse(self):
        try:
            categories = self.getCategory()
            result = {
                "url": {}
            }

            for ammo in self.availableAmmo:
                url = categories[ammo]
                data = self.getStructure(url)

                result[ammo] = data
                result["url"][ammo] = url

            result["time"] = self.getCurrentTime()

            self.saveData(self.dataFile, json.dumps(result))
        except Exception as e:
            print e
        finally:
            print "Parse %s successful" % (self.shopName)
    