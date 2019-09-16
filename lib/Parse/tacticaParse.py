# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re
import urllib

class TacticaParseData(ParseData):
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
        self.categoriesCompare = settings["categories_compare"]
        self.url = settings["url"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanPriceNum(self, price):
        priceRe = re.search("([0-9-\.]+) %s" % (u"грн."), price)
        priceVal = priceRe.group(1)
        priceNum = float(priceVal)

        return priceNum if priceNum != 0 else None

    def cleanTitle(self, title):
        title = title.replace(u"Набій нарізний мисливський ", "")
        title = title.replace(u"Набій нарізний спортивний ", "")
        title = title.replace(u"Набій нарізний ", "")

        return title;

    def getNumCategoryByName(self, category):
        for key, value in self.categories.items():
            if value == category:
                return self.categoriesCompare[key]

    def getStructure(self, url):
        result = []
        # page = self.requestsUrllib2Page(url)
        # blocks = page.xpath('//div[@class="product"]')
        idRe = re.search("\&a\_val\=\[\[(.+)\]\]", url)
        idVal = idRe.group(1)
        value = idVal.split(':')[1]

        categoryRe = re.search("ammunition\/([a-z]+)\/", url)
        categoryVal = categoryRe.group(1)
        category = self.getNumCategoryByName(categoryVal)

        requests = self.requestsPost("https://tactica.kiev.ua/index.php?route=module/filter_products/getProductsByCategory", {
            "category_id": category,
            "manufacturer_id": "0",
            "sort": "p.price",
            "order": "DESC",
            "limit": "100",
            "page": "1",
            "path": "189_67_69",
            "p_val[min]": "0",
            "p_val[max]": "2",
            "a_val[33][]": urllib.unquote(value)
        })
        data = requests.json()

        if 'products' in data:
            for item in data['products']:
                dic = {}
                price = self.cleanPriceNum(item['price'])

                if price:
                    dic["title"] = self.cleanTitle(item['name'])
                    dic["price"] = price

                    result.append(dict(dic))

        return sorted(result, key=self.sortArrayByPrice)
    