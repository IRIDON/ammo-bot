# -*- coding: utf-8 -*-
import json
from telebot import types
from lib.Constructor.botConstructor import BotConstructor
from lib.Botan import botan

class TelegramConstructor(BotConstructor):
    __slots__ = [
        "bot",
        "botHelpFile",
        "currency",
        "availableDiscount",
        "categories",
        "message",
        "availableAmmo",
        "botanApiKey",
        "discount",
        "visibleTopItems",
        "categoriesKeys",
        "shopData",
        "currentShop",
        "availableShops",
        "dataFileUrl"
    ]
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.botHelpFile = kwargs["helpFile"]
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.botanApiKey = kwargs["apiKey"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.availableShops = self.shopData.keys()
        self.discount = 0
        self.visibleTopItems = kwargs["resultItemCount"]
        self.currentShop = self.availableShops[0]
        self.initShopData(self.currentShop)

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

            key = types.InlineKeyboardButton(
                text=self.getKeyName(text),
                callback_data=callback + '_' + str(index)
            )
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
        self.bot.send_message(
            id,
            message,
            parse_mode="HTML",
            reply_markup=markup
        )

    def botAnswerCallback(self, id):
        self.bot.answer_callback_query(id)

    def botChooseKeyboard(self, chat, message, name, keyboard, text):
        analyticMessage = self.getKeyName(name)
        analyticMessage = analyticMessage[:1].upper() + analyticMessage[1:]

        self.botSendMessage(
            chat.id,
            text,
            keyboard
        )
        self.botan(
            chat.id,
            message,
            analyticMessage
        )

    def botSelectStore(self, message):
        try:
            shopName = []

            for shop in self.availableShops:
                shopName.append(shop.upper())
                
            keyboard = self.getBotInlineKeyboards(shopName, 'shop')

            self.botSendMessage(
                message.chat.id,
                self.message["choose_shop"],
                keyboard
            )
            self.botan(
                message.chat.id,
                message,
                self.message["choose_shop"]
            )
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


            self.botChooseKeyboard(
                message.chat,
                message,
                "choose_caliber",
                keyboard,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper())
            )
        except Exception as e:
            print e

    def botSwitchShop(self, callData):
        try:
            data = callData.data.split('_')
            self.currentShop = self.availableShops[int(data[1])]

            self.botAnswerCallback(callData.id)
            self.initShopData(self.currentShop)
        except Exception as e:
            print e

    def botCallTop(self, callData):
        try:
            data = callData.data.split('_')
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = self.topPrices(
                self.visibleTopItems,
                currentCaliber,
                self.discount
            )

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as e:
            print e

    def botComandDiscount(self, message):
        try:
            keyboard = self.getBotInlineKeyboards(self.availableDiscount, 'discount')

            self.botChooseKeyboard(
                message.chat,
                message,
                "choose_discount",
                keyboard,
                self.message["choose_discount"]
            )
        except Exception as e:
            print e
    
    def botCallDiscount(self, callData):
        try:
            data = callData.data.split('_')
            self.discount = self.availableDiscount[int(data[1])]
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top')

            self.botAnswerCallback(callData.id)
            self.botChooseKeyboard(
                callData.message.chat,
                callData.message,
                "choose_caliber",
                keyboard,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper())
            )
        except Exception as e:
            print e

    def botComandMedian(self, message):
        try:
            self.discount = 0
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'median')

            self.botChooseKeyboard(
                message.chat,
                message,
                "choose_caliber",
                keyboard,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper())
            )
        except Exception as e:
            print e

    def botCallMedian(self, callData):
        try:
            data = callData.data.split('_')
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = "Mediana for %s - <b>%s %s</b>" % (
                self.getKeyName(currentCaliber),
                self.median(currentCaliber),
                self.currency
            )

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as e:
            print e
