from lib.parseData import ParseData
from lxml import html
import json

class IbisParseData(ParseData):
    __slots__ = ["categories", "dataFileUrl", "availableAmmo", "urlTmp", "shopName"]
    def __init__(self, settings):
        self.shopName = settings["shop_name"]
        self.categories = settings["category"]
        self.dataFileUrl = settings["data_file"]
        self.availableAmmo = settings["ammo_type"]
        self.urlTmp = settings["url_tmp"]

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
            self.saveData(self.dataFileUrl, json.dumps(data))
        except Exception as e:
            print e
        finally:
            print "%s %s" % ("Parse successful", self.shopName)

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
