# -*- coding: utf-8 -*-

"""
Parse data from websile ibis.net.ua
create JSON data and save it in file
"""
import requests
from lxml import html
import json
import time

class ParseData(object):
    def __init__(self):
        self.shopName = ""

    def coder(self, text):
        return text.encode('utf-8')

    def decoder(self, text):
        return text.decoder('utf-8')

    def requestsPage(self, url):
        page = requests.get(url)

        return html.fromstring(page.content)

    def getData(self, url):
        page = requests.get(url)
        tree = html.fromstring(page.content)
        price = self.getPrices(tree)
        data = self.getStructure(tree, price)

        return data

    def saveData(self, dataFileUrl, dataJson):
        with open(dataFileUrl, "w") as file:
            file.truncate() #clean file data
            file.write(str(dataJson))

    def getCurrentTime(self):
        timetup = time.gmtime(time.time() + 3 * 60 * 60)
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', timetup)

        return currentTime
