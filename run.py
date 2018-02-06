# -*- coding: utf-8 -*-
from config import settings
import telebot, time
from telebot import types
from lib.Constructor.telegramConstructor import TelegramConstructor
from lib.Logger.logger import Log

log = Log()

bot = telebot.TeleBot(settings.API_TOKEN)
commands = ''
botConstructor = TelegramConstructor(
    bot,
    helpFile=settings.BOT_HELP_FILE,
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=settings.MESSAGE,
    calibersAll=settings.CALIBERS,
    apiKey=settings.BOTAN_API,
    shopData=settings.SHOPS,
    resultItemCount=settings.RESULT_ITEMS_COUNT,
    allResultItemCount=settings.ALL_RESULT_ITEMS_COUNT,
)
@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    botConstructor.botComandStart(message)

@bot.message_handler(commands=['top', 'discount'])
def sendTop(message):
    global commands
    commands = message.text.replace("/", "")

    botConstructor.botSelectStore(message)

@bot.message_handler(commands=['all'])
def sendTop(message):
    botConstructor.botComandAll(message)

@bot.callback_query_handler(func=lambda call: call.data.find("shop") != -1)
def callTop(call):
    global commands
    botConstructor.botSwitchShop(call)

    if commands == 'top':
        botConstructor.botComandTop(call.message)
    elif commands == 'discount':
        botConstructor.botComandDiscount(call.message)

@bot.callback_query_handler(func=lambda call: call.data.find("top") != -1)
def callTop(call):
    botConstructor.botCallTop(call)

@bot.callback_query_handler(func=lambda call: call.data.find("discount") != -1)
def callDiscount(call):
    botConstructor.botCallDiscount(call)

@bot.callback_query_handler(func=lambda call: call.data.find("all") != -1)
def callAll(call):
    botConstructor.botCallAll(call)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        botConstructor.botSendMessage(message.chat.id, settings.MESSAGE["empy"])
    except Exception as error:
        botConstructor.botSendMessage(message.chat.id, 'Opppsss!')
        log.error(error)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as error:
        log.error(error)

        time.sleep(15)
