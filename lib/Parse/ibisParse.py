# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
import re

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
        price = tree.xpath('.//div[contains(@class, "pb_price")]')
        priceText = price[0].xpath('./text()')

        if len(priceText[0].strip()):
            return float(priceText[0])
        else:
            pn = price[0].xpath('*/text()')

            return float(pn[0] + pn[1])

    def getStructure(self, url):
        result = []
        page = self.requestsPage(url)
        blocks = page.xpath('.//form[@class="product_brief_list "]')

        for item in blocks:
            price = self.getPrices(item)

            if price:
                dic = {}
                amountCategory = self.availableAmmo['22_LR'][0];
                name = item.xpath('.//a[@class="pb_product_name"]/text()')

                if(url.find(amountCategory) != -1):
                    amount = 1;
                    extra = item.xpath('.//div[@class="pb_extra"]/text()')
                    extraStr = ','.join(extra)

                    amountRe = re.search("([0-9]+) ?%s" % (u"шт"), extraStr)

                    if amountRe:
                        amount = int(amountRe.group(1))

                    calcPrice = round(price / amount, 2)

                    if (calcPrice < 1):
                        calcPrice = price

                    price = calcPrice

                dic["title"] = name[0].encode('utf-8').strip()
                dic["price"] = price

                result.append(dict(dic))
            else:
                break

        return sorted(result, key=self.sortArrayByPrice)
