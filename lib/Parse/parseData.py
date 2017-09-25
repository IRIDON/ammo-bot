# -*- coding: utf-8 -*-

"""
Parse data from websile ibis.net.ua
create JSON data and save it in file
"""
from lib.Logger import log
import requests, logging
from lxml import html
import json
import time

logging.basicConfig(
    format = u'%(levelname)-8s [%(asctime)s] %(message)s',
    level = logging.ERROR,
    filename = '%s/log/log.log' % (path)
)
log = logging

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
        page = requests.get(url)

        return html.fromstring(page.content)

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

    def parse(self):
        try:
            result = {
                "url": {}
            }

            for ammo in self.availableAmmo:
                url = self.getUrl(ammo)
                data = self.getStructure(url)

                result[ammo] = data
                result["url"][ammo] = url

            result["time"] = self.getCurrentTime()

            self.saveData(self.dataFile, json.dumps(result))
        except Exception as error:
            log.error(error)
        finally:
            log.info(u"Parse %s successful" % (self.shopName))
