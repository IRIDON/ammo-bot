# -*- coding: utf-8 -*-
import json
from telebot import types
from lib.Constructor.botConstructor import BotConstructor
from lib.Logger.logger import Log
from lib.Base import Base
from config import settings

log = Log()
base = Base(dataFile=settings.DATA['DISCONT'])

class TelegramConstructor(BotConstructor):
    __slots__ = [
        "bot",
        "botHelpFile",
        "currency",
        "availableDiscount",
        "categories",
        "message",
        "availableAmmo",
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
        self.message = kwargs["message"]
        self.shopData = kwargs["shopData"]
        self.calibersAll = kwargs["calibersAll"]
        self.dataUpdateTime = ''
        self.availableShops = self.getAvailableShops()
        self.visibleTopItems = kwargs["resultItemCount"]
        self.allResultItemCount = kwargs["allResultItemCount"]
        self.currentShop = self.availableShops[0]
        self.initShopData(self.currentShop)

    def getAvailableShops(self):
        data = self.shopData.keys()

        return sorted(data)

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
        self.botSendMessage(
            chat.id,
            text,
            keyboard
        )

    def botSelectStore(self, message, name):
        try:
            discountData = self.getDiscountData(message)
            shopName = []

            for shop in self.availableShops:
                shopUpper = shop.upper()
                isDiscount = discountData and shop in discountData

                if isDiscount:
                    template = "%s - %s%s" % (shopUpper, discountData[shop], '%')
                else:
                    template = shopUpper

                shopName.append(template)

            keyboard = self.getBotInlineKeyboards(shopName, name)

            self.botSendMessage(
                message.chat.id,
                self.message["choose_shop"],
                keyboard
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

    def botComandTop(self, callData):
        try:
            self.botSwitchShop(callData)

            message = callData.message
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
            self.currentShop = self.getShopNameFromIndex(callData)

            self.botAnswerCallback(callData.id)
            self.initShopData(self.currentShop)
        except Exception as error:
            log.error(error)

    def botCallTop(self, callData):
        try:
            discountData = self.getDiscountData(callData)
            data = callData.data.split('_')
            currentCaliber = self.categoriesKeys[int(data[1])]

            result = self.topPrices(
                self.visibleTopItems,
                currentCaliber,
                discountData
            )

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as error:
            log.error(error)

    def botComandDiscount(self, callData):
        try:
            message = callData.message
            shop = self.getShopNameFromIndex(callData)
            keyboard = self.getBotInlineKeyboards(self.availableDiscount, 'discount_' + shop)

            self.botChooseKeyboard(
                message.chat,
                message,
                "choose_discount",
                keyboard,
                self.message["choose_discount"]
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
            discountData = self.getDiscountData(callData)
            data = callData.data.split('_')
            currentCaliber = self.calibersAll[int(data[1])]

            result = self.allShopPrices(currentCaliber, self.allResultItemCount, discountData)

            self.botAnswerCallback(callData.id)
            self.botSendMessage(callData.message.chat.id, result)
        except Exception as error:
            log.error(error)

    def getShopNameFromIndex(self, callData):
        data = callData.data.split('_')

        return self.availableShops[int(data[1])]

    def getDiscountData(self, message):
        return base.get(message.from_user.id)

    def setDiscontToBase(self, callData):
        data = callData.data.split('_')
        shop = data[1]
        discountIndex = int(data[2])
        discount = self.availableDiscount[discountIndex]

        base.set(callData.from_user.id, shop, discount)
        self.botSendMessage(callData.message.chat.id, 'Discount set!')
        self.botComandStart(callData.message);

