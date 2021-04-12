# -*- coding: utf-8 -*-

"""
Parse data from websile ibis.net.ua
create JSON data and save it in file
"""
import requests, urllib2, logging, time, json
from lxml import html
from lib.Logger.logger import Log
import re

log = Log()

class ParseData(object):
    def __init__(self):
        self.shopName = ""

    def coder(self, text):
        return text.encode('utf-8')

    def decoder(self, text):
        return text.decoder('utf-8')

    def sortArrayByPrice(self, x):
        return x["price"]

    def requestsPage(self, url):
        page = requests.get(url, verify=False)

        return html.fromstring(page.content)

    def requestsPost(self, url, data):
        return requests.post(url, verify=False, data=data)

    def requestsPostPage(self, url, data):
        page = requests.post(url, verify=False, data=data)

        return html.fromstring(page.content)

    def requestsUrllib2Page(self, url):
        try:
            response = urllib2.urlopen(url)
            page = response.read()

            return html.fromstring(page)
        except Exception as error:
            log.error(error)

    def get_link_response_code(link_to_check):
        resp = requests.head(link_to_check)

        if resp.status_code == 405:
            resp = requests.get(link_to_check)
            
        return resp.status_code

    def getHourInSeconds(self, hour):
        return hour * 60 * 60

    def getUrl(self, id):
        ammo = self.availableAmmo[id]
        category = ammo[1]
        key = ammo[0]
        part = self.categories[category]

        return self.urlTmp % (part, key)

    def saveData(self, dataFileUrl, dataJson):
        with open(dataFileUrl, "w") as file:
            file.truncate() #clean file data
            file.write(str(dataJson))

    def getCurrentTime(self):
        timetup = time.gmtime(time.time() + self.getHourInSeconds(3))
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', timetup)

        return currentTime

    def cleanPriceNum(self, price):
        if " " in price:
            price = price.split(" ")[0]

        price = re.sub('[^0-9a-zA-Z]+', '.', price)
        print(price)
        if price[len(price) - 1] == '.':
            price = price[:-1]

        if price[0] == '.':
            price = price[1:]

        return float(price)

    def cleanTitle(self, title):
        title = title.replace(u"Патрон нарезной ", "")
        title = title.replace(u"Патрон ", "")
        title = title.replace(u" /", "/")

        return title;

    def getAmount(self, string):
        amount = 1;
        amountRe = re.search("([0-9]+) ?%s" % (u"шт"), string)

        if amountRe:
            amount = int(amountRe.group(1))

        return amount

    def getPriceByAmount(self, price, amount):
        calcPrice = round(price / amount, 2)

        if (calcPrice < 1):
            calcPrice = price

        return calcPrice

    def parse(self):
        result = {
            "url": {}
        }
        count = 0

        for ammo in self.availableAmmo:
            url = self.getUrl(ammo)
            data = self.getStructure(url)
            
            count += len(data)
            result[ammo] = data
            result["url"][ammo] = url

        result["time"] = self.getCurrentTime()

        self.saveData(self.dataFile, json.dumps(result))
