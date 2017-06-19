# -*- coding: utf-8 -*-
from config import settings
import telebot
from telebot import types
from lib.botConstructor import BotConstructor

bot = telebot.TeleBot(settings.API_TOKEN)
commands = ''
botConstructor = BotConstructor(
    bot,
    helpFile=settings.BOT_HELP_FILE,
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=settings.MESSAGE,
    apiKey=settings.BOTAN_API,
    availableShops=settings.AVAILABLE_SHOPS,
    shopData=settings.SHOPS,
    resultItemCount=settings.RESULT_ITEMS_COUNT,
)
@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    botConstructor.botComandStart(message)

@bot.message_handler(commands=['discount'])
def sendDiscont(message):
    botConstructor.botComandDiscount(message)

@bot.message_handler(commands=['top'])
def sendTop(message):
    botConstructor.botSelectStore(message)
    # botConstructor.botComandTop(message)

@bot.message_handler(commands=['median'])
def sendTop(message):
    botConstructor.botComandMedian(message)


@bot.callback_query_handler(func=lambda call: call.data.find("shop") != -1)
def callTop(call):
    botConstructor.botSwitchShop(call)
    botConstructor.botComandTop(call.message)

@bot.callback_query_handler(func=lambda call: call.data.find("top") != -1)
def callTop(call):
    botConstructor.botCallTop(call)

@bot.callback_query_handler(func=lambda call: call.data.find("discount") != -1)
def callDiscount(call):
    botConstructor.botCallDiscount(call)

@bot.callback_query_handler(func=lambda call: call.data.find("median") != -1)
def callTop(call):
    botConstructor.botCallMedian(call)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        botConstructor.botSendMessage(message.chat.id, settings.MESSAGE["empy"])
    except Exception as e:
        botConstructor.botSendMessage(message.chat.id, 'Opppsss!')
        print e

bot.polling()
