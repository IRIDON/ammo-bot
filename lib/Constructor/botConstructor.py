# -*- coding: utf-8 -*-
import json
import statistics
from config import settings

default_lang = settings.DEFAULT_LANG

class BotConstructor(object):
    __slots__ = [
        "currency",
        "message",
        "shopData",
        "dataUpdateTime",
        "shopName"
    ]
    def __init__(self, **kwargs):
        self.currency = kwargs["currency"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.dataUpdateTime = ''

    def initShopData(self, shopName):
        if self.shopData[shopName]:
            shopData = self.shopData[shopName]

            self.shopName = shopName;
            self.categories = sorted(shopData["category"].items(), key=lambda item: item[1][2])
            self.categoriesKeys = map(lambda x: x[0], self.categories)
            self.availableAmmo = shopData["ammo_type"]
            self.dataFileUrl = shopData["data_file"]
        else:
            return False

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return float(format(price * factor, '.2f'))

    def getLanguage(self, data):
        user_data = data.from_user
        language_code = user_data.language_code

        if not language_code:
            return default_lang

        if language_code.find('-') != -1:
            return language_code.split('-')[0].lower()
        else:
            return language_code

        return default_lang

    def getString(self, key, language=default_lang):
        if not language in self.message:
            language = default_lang

        message = self.message[language]

        if key in message:
            return message[key]
        else:
            return key

    def chunkArr(self, seq, num):
        num = len(seq) / num
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out

    def topPrices(self, num=3, category='', discountData={}, language=default_lang):
        discount = self.getDiscontFromData(discountData, self.shopName)
        allData = self.getData()

        if not allData:
            return self.getString("base_error", language)

        data = allData[category]

        self.dataUpdateTime = allData["time"]
        
        if discount:
            for item in data:
                itemPrice = item['price']
                item['origin_price'] = itemPrice
                item['price'] = self.getDiscount(itemPrice, discount)

        data = sorted(data, key=lambda x: x["price"])

        result = self.formateResult(
            data,
            num,
            category,
            discount,
            language
        )

        url = self.getCategoryUrl(allData["url"][category])

        result.append("\n<a href='%s'>%s</a>" % (
            url,
            self.getString("link_text", language)
        ))

        return "\n".join(result)

    def allShopPrices(self, category, num=10, discountData={}, language=default_lang):
        result = self.allPrices(category, num, discountData, language)

        if not result:
            return self.getString("base_error", language)

        return "\n".join(result)

    def formateResult(self, data, num=3, category='', discount=0, language=default_lang, urls=None):
        result = []
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        categoryName = self.getKeyName(category)

        if discount:
            title = "<b>%s</b> <i>-%s&#37;</i>\n" % (categoryName, discount)
        else:
            title = "<b>%s</b>\n" % (categoryName)

        result.append(title)

        for index in range(0, num):
            item = data[index]
            shopName = item.get('shop_name')
            title = item["title"]
            price = item["price"]
            isDiscount = 'origin_price' in item
            template = "<b>%s %s</b> - %s"
            resultArr = [price, self.currency, title]

            if isDiscount and not shopName:
                template = "<b>%s %s</b> <i>(%s)</i> - %s"
                resultArr = (
                    price,
                    self.currency,
                    item["origin_price"],
                    title
                )
            elif isDiscount and shopName:
                template = "<b>%s %s</b> <i>(%s)</i> - %s (%s)"
                resultArr = (
                    price,
                    self.currency,
                    item["origin_price"],
                    title,
                    shopName
                )
            elif shopName:
                template = "<b>%s %s</b> - %s (%s)"
                resultArr.append(shopName)

            result.append(template % tuple(resultArr))


        if len(result) == 1:
            result.append(self.getString("no_results", language))


        test = self.getString("base_date", language)

        if self.dataUpdateTime:
            result.append("\n<i>%s: %s</i>" % (
                self.getString("base_date", language),
                self.dataUpdateTime
            ))

        if urls:
            result.append("\n" + self.getAllUrl(urls, language))

        return result

    def allPrices(self, caliber, num, discountData, language):
        data = self.shopData
        result = []
        dataFiles = []
        urls = {}

        for shopName in self.shopData:
            discount = self.getDiscontFromData(discountData, shopName)
            shop = data[shopName]

            with open(shop["data_file"], "r") as file:
                shopData = json.load(file)

                if not self.dataUpdateTime:
                    self.dataUpdateTime = shopData['time']

                if caliber in shopData:
                    url = shopData['url'][caliber]

                    urls[shopName] = url

                    for item in shopData[caliber]:
                        item['shop_name'] = shop['shop_name'].upper()

                        if discount:
                            itemPrice = item['price']

                            item['origin_price'] = itemPrice
                            item['price'] = self.getDiscount(itemPrice, discount)

                        dataFiles.append(item)
        
        dataFiles = sorted(dataFiles, key=lambda x: x["price"])

        return self.formateResult(
            dataFiles,
            num,
            caliber,
            0,
            language,
            urls
        )

    def getKeyName(self, name):
        return name.replace("_", " ")

    def getCategoryUrl(self, url):
        utmSeparator = '?' if url.find('?') == -1 else '&'

        return  url + utmSeparator + "utm_source=ammoBot"

    def getAllUrl(self, urls, language):
        urlsText = []
        
        for key, value in urls.iteritems():
            url = self.getCategoryUrl(value)

            urlsText.append("<a href='%s'>%s</a>" % (
                url,
                self.getString("link_tmp", language) % key
            ))

        return " - ".join(urlsText)

    def getDiscontFromData(self, data, shopName):
        discount = 0

        if not data:
            return discount

        discountFromData = data.get(shopName.lower())

        if discountFromData:
            discount = discountFromData

        return discount


    def toSeconds(day):
        return day * 24 * 60 * 60
    