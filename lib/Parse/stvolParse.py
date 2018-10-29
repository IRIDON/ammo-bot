# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
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
    def __init__(self, settings):
        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanPriceNum(self, price):
        price = price.split(" ")[0]
        price = re.sub('[^0-9a-zA-Z]+', '.', price)

        if price[len(price) - 1] == '.':
            price = price[:-1]

        return float(price)

    def getAmount(self, blocks):
        for text in blocks:
            amountRe = re.search("([0-9]+) %s" % (u"шт"), text)

            print(text)

            if amountRe:
                return int(amountRe.group(1))
            else:
                return 1

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//div[@class="cover-tov"]')

        for item in blocks:
            dic = {}
            name = item.xpath('.//a[@class="tov-name"]/text()')
            price_1 = item.xpath('.//div[@class="current-price"]/b/text()')[0].replace(' ', '')
            price_2 = item.xpath('.//div[@class="current-price"]/text()')[0]
            avilible = item.xpath('.//div[@class="no-item"]')

            if len(avilible) == 0:
                price = self.cleanPriceNum(price_1 + price_2) 
                amountCategory = self.availableAmmo['22_LR'][0];

                if(url.find(amountCategory) != -1):
                    amount = 1
                    amountTexts = item.xpath('.//div[@class="tov-option-line"]//text()')

                    for text in amountTexts:
                        amountRe = re.search("([0-9]+) %s" % (u"шт"), text)

                        if amountRe:
                            amount =  int(amountRe.group(1))

                    calcPrice = round(price / amount, 2)

                    if (calcPrice < 1):
                        calcPrice = price

                    price = calcPrice

                dic["title"] = self.cleanTitle(name[0])
                dic["price"] = price

                result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    