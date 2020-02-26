# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re
from config.shops import shops
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
    def __init__(self):
        settings = shops["tactica"]

        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.availableAmmo = settings["category"]
        self.categoriesCompare = settings["categories_compare"]
        self.url = settings["url"]
        self.urlRequest = settings["url_request"]
        self.urlTmp = settings["url_tmp"]
        self.dataFile = settings["data_file"]

    def cleanTitle(self, title):
        title = title.replace(u"Набій нарізний мисливський ", "")
        title = title.replace(u"Набій нарізний спортивний ", "")
        title = title.replace(u"Набій мисливський ", "")
        title = title.replace(u"Набій спортивний ", "")
        title = title.replace(u"Набій нарізний ", "")
        title = title.replace(u"Набій ", "")
        title = title.replace(u" / ", "/")

        return title;

    def getNumCategoryByName(self, category):
        for key, value in self.categories.items():
            if value == category:
                compare = self.categoriesCompare

                return compare[key] if key in compare else None

    def getValueFromUrl(self, url):
        idRe = re.search("\&a\_val\=\[\[(.+)\]\]", url)
        idVal = idRe.group(1)

        if idVal:
            return idVal.split(':')[1]
        else:
            return None

    def getCategoryFromUrl(self, url):
        categoryRe = re.search("ammunition\/([a-z]+)\/", url)
        categoryVal = categoryRe.group(1)

        if categoryVal:
            return self.getNumCategoryByName(categoryVal)
        else:
            return None

    def getStructure(self, url):
        result = []
        value = self.getValueFromUrl(url)
        category = self.getCategoryFromUrl(url)
        requestData = {
            "manufacturer_id": "0",
            "sort": "p.price",
            "order": "DESC",
            "limit": "100",
            "page": "1",
            "path": "189_67_69",
            "p_val[min]": "0",
            "p_val[max]": "2",
        }

        if not value and not category:
            return;

        requestData["category_id"] = category
        requestData["a_val[33][]"] = urllib.unquote(value)

        requests = self.requestsPost(self.urlRequest, requestData)
        data = requests.json()

        if 'products' in data:
            for item in data['products']:
                dic = {}
                price = self.cleanPriceNum(item['price'])

                if price:
                    dic["title"] = self.cleanTitle(item['name'])
                    dic["price"] = price

                    result.append(
                        dict(dic)
                    )

        return sorted(result, key=self.sortArrayByPrice)
    