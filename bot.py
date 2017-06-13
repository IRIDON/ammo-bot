# -*- coding: utf-8 -*-
from config import default_settings as settings
import telebot
from telebot import types
from lib.botConstructor import BotConstructor

bot = telebot.TeleBot(settings["API_TOKEN"])
botConstructor = BotConstructor(bot)

@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    botConstructor.botComandStart(message)

@bot.message_handler(commands=['discount'])
def sendDiscont(message):
    botConstructor.botComandDiscount(message)

@bot.message_handler(commands=['top'])
def sendTop(message):
    botConstructor.botComandTop(message)

@bot.message_handler(commands=['median'])
def sendTop(message):
    botConstructor.botComandMedian(message)


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
        botConstructor.botSendMessage(message.chat.id, settings["MESSAGE"]["empy"])
    except Exception as e:
        botConstructor.botSendMessage(message.chat.id, 'Opppsss!')
        print e

bot.polling()
