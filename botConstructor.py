# -*- coding: utf-8 -*-
from __init__ import *
import json
from telebot import types

class BotConstructor(object):
    def __init__(self, bot):
        self.bot = bot
        self.botHelpFile = BOT_HELP_FILE
        self.dataFileUrl = DATA_FILE
        self.currency = CURRENCY
        self.availableDiscount = DISCONT
        self.categories = CALIBERS
        self.message = MESSAGE
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

        return URL_TMP % (AMMO_TYPE[category[1]], category[0])

    def topPrices(self, num=3, category='', discount=0):
        result = []
        data = self.getData()
        data = data[category]
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
        
        result.append("\n[Visit to site](%s)" % (self.getUrl(category)))
        
        return "\n".join(result)

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
            text = str(text)

            key = types.InlineKeyboardButton(text=text.replace("_", " "), callback_data=callback + '_' + str(index))
            markup.add(key)

        return markup

    def botSendMessage(self, id, message, markup=''):
        self.bot.send_message(id, message, parse_mode="Markdown", reply_markup=markup)

    def botAnswerCallback(self, id):
        self.bot.answer_callback_query(id)

    def botComandStart(self, message):
        with open(self.botHelpFile, "r") as helpFile:
            helpText = helpFile.read()

            self.botSendMessage(message.chat.id, helpText)

    def botComandTop(self, message):
        self.discount = 0
        keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top')

        self.botSendMessage(message.chat.id, self.message["choose_caliber"], keyboard)

    def botCallTop(self, callData):
        data = callData.data.split('_')
        currentCaliber = self.categoriesKeys[int(data[1])]

        result = self.topPrices(self.visibleTopItems, currentCaliber, self.discount)

        self.botAnswerCallback(callData.id)
        self.botSendMessage(callData.message.chat.id, result)

    def botComandDiscount(self, message):
        keyboard = self.getBotInlineKeyboards(self.availableDiscount, 'discount')

        self.botSendMessage(message.chat.id, self.message["choose_discount"], keyboard)
    
    def botCallDiscount(self, callData):
        data = callData.data.split('_')
        self.discount = self.availableDiscount[int(data[1])]
        keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top')

        self.botAnswerCallback(callData.id)
        self.botSendMessage(callData.message.chat.id, self.message["choose_caliber"], keyboard)

