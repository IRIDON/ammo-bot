# -*- coding: utf-8 -*-

from lib.Parse.parseData import ParseData
from lxml import html
from config.shops import shops
import re

class IbisParseData(ParseData):
    __slots__ = [
        "url",
        "ammo_type",
        "dataFile",
        "availableAmmo",
        "urlTmp",
        "shopName"
    ]
    def __init__(self):
        settings = shops["ibis"]

        self.url = settings["url"]
        self.shopName = settings["shop_name"]
        self.categories = settings["ammo_type"]
        self.dataFile = settings["data_file"]
        self.availableAmmo = settings["category"]
        self.urlTmp = settings["url_tmp"]

    def getPrices(self, tree):
        priceBlock = tree.xpath('.//div[contains(@class, "pb_price")]')
        price = priceBlock[0]
        priceText = price.xpath('./text()')

        if len(priceText[0].strip()):
            return float(priceText[0])
        else:
            pn = price.xpath('*/text()')

            return float(pn[0] + pn[1])

    def getAmount(self, string):
        amount = 1;
        amountRe = re.search("([0-9]+) ?%s" % (u"шт"), string)

        if amountRe:
            amount = int(amountRe.group(1))
        else:
            amount = float(string)

        return amount

    def getAmountFromUrl(self, url):
        page = self.requestsPage(self.url + url)
        blocks = page.xpath('.//*[@class="prod_extra_table"]/tr')

        for item in blocks:
            text = item.xpath('./td/b/text()')

            if text and u'шт' in text[0]:
                secondItem = item.xpath('./td')[1]
                secondItemText = secondItem.xpath('./text()')

                return self.getAmount(
                    secondItemText[0]
                )

    def getPageData(self, page, url):
        result = []
        amountCategory = self.availableAmmo['22_LR'][0]
        blocks = page.xpath('.//form[@class="product_brief_list "]')
        
        for item in blocks:
            price = self.getPrices(item)

            if price:
                dic = {}
                nameBlock = item.xpath('.//a[@class="pb_product_name"]/text()')
                name = nameBlock[0]
                
                if(amountCategory in url):
                    itemUrl = item.xpath('.//a[@class="pb_product_name"]/@href')
                    amount = self.getAmountFromUrl(itemUrl[0])
                    price = self.getPriceByAmount(price, amount if amount else 1)

                dic["title"] = self.cleanTitle(name).encode('utf-8').strip()
                dic["price"] = price

                result.append(
                    dict(dic)
                )
            else:
                break

        return result

    def getStructure(self, url):
        page = self.requestsPage(url)
        paginationsPage = page.xpath('.//div[@class="category_nav"]/a[@class="page_num"]/@href')
        result = self.getPageData(page, url)
        
        if len(paginationsPage) != 0:
            for pageUrl in paginationsPage:
                fullUrl = self.url + pageUrl
                itemPage = self.requestsPage(fullUrl)

                result = result + self.getPageData(itemPage, fullUrl)

        return sorted(result, key=self.sortArrayByPrice)
