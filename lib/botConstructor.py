# -*- coding: utf-8 -*-
from config import default_settings as settings
import json
from telebot import types
import statistics
import botan

class BotConstructor(object):
    def __init__(self, bot):
        self.bot = bot
        self.botHelpFile = settings["BOT_HELP_FILE"]
        self.dataFileUrl = settings["DATA_FILE"]
        self.currency = settings["CURRENCY"]
        self.availableDiscount = settings["DISCONT"]
        self.categories = settings["CALIBERS"]
        self.message = settings["MESSAGE"]
        self.availableAmmo = settings["AMMO_TYPE"]
        self.botanApiKey = settings["BOTAN_API"]
        self.urlTmp = settings["URL_TMP"]
        self.discount = 0
        self.visibleTopItems = 5
        self.categoriesKeys = self.categories.keys()

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return format(price * factor, '.2f')

    def getUrl(self, categoryName):
        category = self.categories[categoryName]

        return self.urlTmp % (self.availableAmmo[category[1]], category[0])

    def topPrices(self, num=3, category='', discount=0):
        result = []
        allData = self.getData()
        data = allData[category]
        dataLen = len(data)

        if dataLen < num:
            num = dataLen

        for index in range(0,num):
            title = data[index]["title"]
            price = data[index]["price"]

            if discount == 0:
                result.append("*%s %s* - %s" % (price, self.currency, title))
            else:
                result.append("*%s %s* _(%s)_ - %s" % (self.getDiscount(price, discount), self.currency, price, title))
        
        result.append("\n_%s: %s_" % (self.message["base_date"], allData["time"]))
        result.append("\n[%s](%s)" % (self.message["link_text"], self.getUrl(category) + "?utm_source=ammoBot"))
        
        return "\n".join(result)

    def median(self, category):
        data = self.getData()
        data = data[category]
        prices = []

        for item in data:
            prices.append(item["price"])

        return statistics.median_low(prices)

    def toSeconds(day):
        return day * 24 * 60 * 60

    def getBotKeyboards(self, array):
        markup = types.ReplyKeyboardMarkup(row_width=1)

        for key in array:
            markup.add(types.KeyboardButton(key))

        return markup

    def getBotInlineKeyboards(self, array, callback='call'):
        markup = types.InlineKeyboardMarkup()

        for index, text in enumerate(array):
            if type(text) != str:
                text = str(text) + "%"

            key = types.InlineKeyboardButton(text=text.replace("_", " "), callback_data=callback + '_' + str(index))
            markup.add(key)

        return markup

    def botan(self, id, data, name):
        botan.track(
            token=self.botanApiKey,
            uid=id,
            message=data,
            name=name
        )

    def botSendMessage(self, id, message, markup=''):
        self.bot.send_message(id, message, parse_mode="Markdown", reply_markup=markup)

    def botAnswerCallback(self, id):
        self.bot.answer_callback_query(id)

    def botComandStart(self, message):
        try:
            with open(self.botHelpFile, "r") as helpFile:
                helpText = helpFile.read()

                self.botSendMessage(message.chat.id, helpText)
        except Exception as e:
            print e

    def botComandTop(self, message):
        try:
            self.discount = 0
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top')

            self.botSendMessage(message.chat.id, self.message["choose_caliber"], keyboard)
            self.botan(message.chat.id, message, "Choose caliber")
        except Exception as e:
            print e

    def botCallTop(self, callData):
        try:
            data = callData.data.split('_')
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = self.topPrices(self.visibleTopItems, currentCaliber, self.discount)

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as e:
            print e

    def botComandDiscount(self, message):
        try:
            keyboard = self.getBotInlineKeyboards(self.availableDiscount, 'discount')

            self.botSendMessage(message.chat.id, self.message["choose_discount"], keyboard)
            self.botan(message.chat.id, message, "Choose discount")
        except Exception as e:
            print e
    
    def botCallDiscount(self, callData):
        try:
            data = callData.data.split('_')
            self.discount = self.availableDiscount[int(data[1])]
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top')

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, self.message["choose_caliber"], keyboard)
            self.botan(callData.message.chat.id, callData.message, "Choose caliber")
        except Exception as e:
            print e

    def botComandMedian(self, message):
        try:
            self.discount = 0
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'median')

            self.botSendMessage(message.chat.id, self.message["choose_caliber"], keyboard)
            self.botan(message.chat.id, message, "Choose caliber")
        except Exception as e:
            print e

    def botCallMedian(self, callData):
        try:
            data = callData.data.split('_')
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = "Mediana for %s - *%s %s*" % (currentCaliber, self.median(currentCaliber), self.currency)

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as e:
            print e
    