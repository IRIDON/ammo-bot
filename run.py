# -*- coding: utf-8 -*-
from config import settings
from config.message import message
from config.shops import shops

import telebot, time, apiai, json
from telebot import types
from lib.Constructor.telegramConstructor import TelegramConstructor
from lib.Logger.logger import Log

log = Log()

dialogBot = apiai.ApiAI(settings.AI_API_KEY)

bot = telebot.TeleBot(settings.API_TOKEN)

botConstructor = TelegramConstructor(
    bot,
    currency=settings.CURRENCY,
    discount=settings.DISCONT,
    message=message,
    calibersAll=settings.CALIBERS,
    shopData=shops,
    resultItemCount=settings.RESULT_ITEMS_COUNT,
    allResultItemCount=settings.ALL_RESULT_ITEMS_COUNT,
)
@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    botConstructor.botComandStart(message, None)

@bot.message_handler(commands=['top'])
def sendTop(message):
    botConstructor.botSelectStore(message, 'shop')

@bot.message_handler(commands=['all'])
def sendTop(message):
    botConstructor.botComandAll(message)

@bot.message_handler(commands=['discount'])
def sendTop(message):
    botConstructor.botSelectStore(message, 'select')

@bot.callback_query_handler(func=lambda call: "select" in call.data)
def callDiscount(call):
    botConstructor.botComandDiscount(call)

@bot.callback_query_handler(func=lambda call: "discount" in call.data)
def callDiscount(call):
    botConstructor.setDiscontToBase(call)

@bot.callback_query_handler(func=lambda call: "shop" in call.data)
def callTop(call):
    botConstructor.botComandTop(call)

@bot.callback_query_handler(func=lambda call: "top" in call.data)
def callTop(call):
    botConstructor.botCallTop(call)

@bot.callback_query_handler(func=lambda call: "all" in call.data)
def callAll(call):
    botConstructor.botCallAll(call)


def bot_request(message):
    try:
        request = dialogBot.text_request()
        request.lang = 'ru'
        request.session_id = 'AmmoBot'
        request.query = message
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        botMessage = responseJson['result']['fulfillment']['speech']

        return botMessage if botMessage else "Я Вас не совсем понял!"

    except Exception as error:
        log.error(error)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        response = bot_request(message.text)

        botConstructor.botSendMessage(message.chat.id, response)

    except Exception as error:
        botConstructor.botSendMessage(message.chat.id, 'Opppsss!')
        log.error(error)


if settings.DEV:
    bot.polling(none_stop=True)
else:
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            log.error(error)

            time.sleep(15)
