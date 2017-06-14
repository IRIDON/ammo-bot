# -*- coding: utf-8 -*-

from lib.parseData import ParseData
from lxml import html
import requests
import json

class StvolParseData(ParseData):
    __slots__ = ["categories", "ammo", "availableAmmo", "url", "urlTmp", "dataFile"]
    def __init__(self, settings):
        self.categories = settings["category"]
        self.ammo = settings["ammo"]
        self.availableAmmo = settings["ammo"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

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
            result[name] = link

        return result

    def getCategory(self):
        result = {}

        for category in self.categories:
            categoryUrl = self.getCategoryUrl(category)
            result.update(categoryUrl)

        return result

    def getStructure(self, url):
        result = []
        page = self.requestsPage(self.url + url)
        blocks = page.xpath('.//div[@class="tov-cover"]')

        for item in blocks:
            dic = {}
            name = item.xpath('.//div[@class="tov-name"]/a/text()')
            price_1 = item.xpath('.//div[@class="price"]/b/text()').replace(' ', '')
            price_2 = item.xpath('.//div[@class="price"]/text()')
            price = price_1[0] + price_2[0]
            dic["name"] = name[0]
            dic["price"] = price.split(" ")[0]

            result.append(dict(dic))

        return result

    def parse(self):
        categories = self.getCategory()
        result = {}

        for ammo in self.availableAmmo:
            url = categories[ammo]
            data = self.getStructure(url)

            result[ammo] = data

        self.saveData(self.dataFile, json.dumps(result))
    