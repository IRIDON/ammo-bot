# -*- coding: utf-8 -*-
import json
from telebot import types
from lib.Constructor.botConstructor import BotConstructor
from lib.Botan import botan
from lib.Logger.logger import Log

log = Log()

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
        "allResultItemCount",
        "categoriesKeys",
        "calibersAll",
        "shopData",
        "currentShop",
        "availableShops",
        "dataFileUrl",
        "dataUpdateTime",
    ]
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.botHelpFile = kwargs["helpFile"]
        self.currency = kwargs["currency"]
        self.availableDiscount = kwargs["discount"]
        self.botanApiKey = kwargs["apiKey"]
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.calibersAll = kwargs["calibersAll"]
        self.dataUpdateTime = ''
        self.availableShops = self.shopData.keys()
        self.discount = 0
        self.visibleTopItems = kwargs["resultItemCount"]
        self.allResultItemCount = kwargs["allResultItemCount"]
        self.currentShop = self.availableShops[0]
        self.initShopData(self.currentShop)

    def getBotKeyboards(self, array):
        markup = types.ReplyKeyboardMarkup(row_width=1)

        for key in array:
            markup.add(types.KeyboardButton(key))

        return markup

    def getBotInlineKeyboards(self, array, callback='call', row=1):
        result = []
        markup = types.InlineKeyboardMarkup(row_width=row)

        for index, text in enumerate(array):
            if type(text) != str:
                text = str(text) + "%"

            key = types.InlineKeyboardButton(
                text=self.getKeyName(text),
                callback_data=callback + '_' + str(index)
            )

            result.append(key)

        if row > 1:
            rows = self.chunkArr(result, row)

            for key in rows:
                if len(key) > 1:
                    markup.row(key[0], key[1])
                else:
                    markup.row(key[0])
        else:
            for key in result:
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
        except Exception as error:
            log.error(error)

    def botComandStart(self, message):
        try:
            with open(self.botHelpFile, "r") as helpFile:
                helpText = helpFile.read()

                self.botSendMessage(message.chat.id, helpText)
        except Exception as error:
            log.error(error)

    def botComandTop(self, message):
        try:
            self.discount = 0
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top', 2)

            self.botChooseKeyboard(
                message.chat,
                message,
                "choose_caliber",
                keyboard,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper())
            )
        except Exception as error:
            log.error(error)

    def botSwitchShop(self, callData):
        try:
            data = callData.data.split('_')
            self.currentShop = self.availableShops[int(data[1])]

            self.botAnswerCallback(callData.id)
            self.initShopData(self.currentShop)
        except Exception as error:
            log.error(error)

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
        except Exception as error:
            log.error(error)

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
        except Exception as error:
            log.error(error)
    
    def botCallDiscount(self, callData):
        try:
            data = callData.data.split('_')
            self.discount = self.availableDiscount[int(data[1])]
            keyboard = self.getBotInlineKeyboards(self.categoriesKeys, 'top', 2)

            self.botAnswerCallback(callData.id)
            self.botChooseKeyboard(
                callData.message.chat,
                callData.message,
                "choose_caliber",
                keyboard,
                self.message["choose_caliber_with_shop"] % (self.currentShop.upper())
            )
        except Exception as error:
            log.error(error)

    def botComandAll(self, message):
        try:
            keyboard = self.getBotInlineKeyboards(self.calibersAll, 'all', 2)

            self.botChooseKeyboard(
                message.chat,
                message,
                "all",
                keyboard,
                self.message["choose_caliber"]
            )
        except Exception as error:
            log.error(error)
    
    def botCallAll(self, callData):
        try:
            data = callData.data.split('_')
            currentCaliber = self.calibersAll[int(data[1])]

            result = self.allShopPrices(currentCaliber, self.allResultItemCount)

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as error:
            log.error(error)
