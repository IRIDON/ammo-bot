# -*- coding: utf-8 -*-
import json
from telebot import types
import statistics
import botan

class BotConstructor(object):
    __slots__ = [
        "bot",
        "botHelpFile",
        "currency",
        "availableDiscount",
        "categories",
        "message",
        "availableAmmo",
        "botanApiKey",
        "urlTmp",
        "discount",
        "visibleTopItems",
        "categoriesKeys",
        "availableShops",
        "shopData",
        "dataFileUrl"
    ]
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.botHelpFile = kwargs["helpFile"]
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.botanApiKey = kwargs["apiKey"]
        self.message = kwargs["message"]
        self.availableShops = kwargs["availableShops"]
        self.shopData = kwargs["shopData"]
        # self.urlTmp = kwargs["url"]
        self.discount = 0
        self.visibleTopItems = 5
        self.initShopData(self.availableShops[0])

    def initShopData(self, shopName):
        shopData = self.shopData[shopName]

        self.categories = shopData["category"]
        self.categoriesKeys = self.categories.keys()
        self.availableAmmo = shopData["ammo_type"]
        self.dataFileUrl = shopData["data_file"]
        # if any(shopName in s for s in self.shopData):
            
        # else:
        #     return False

    def getData(self):
        with open(self.dataFileUrl, "r") as file:
            return json.load(file)

    def getDiscount(self, price, discount):
        factor = (100 - float(discount)) / 100

        return format(price * factor, '.2f')

    def topPrices(self, num=3, category='', discount=0):
        result = []
        allData = self.getData()

        if not allData:
            return self.message["base_error"]

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
        result.append("\n[%s](%s)" % (self.message["link_text"], allData["url"][category] + "?utm_source=ammoBot"))
        
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

    def botSelectStore(self, message):
        try:
            keyboard = self.getBotInlineKeyboards(self.availableShops, 'shop')

            self.botSendMessage(message.chat.id, "Choose shop", keyboard)
            self.botan(message.chat.id, message, "Choose shop")
        except Exception as e:
            print e

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

    def botSwitchShop(self, callData):
        try:
            data = callData.data.split('_')
            currentShop = self.availableShops[int(data[1])]

            self.botAnswerCallback(callData.id)
            self.initShopData(currentShop)
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
    