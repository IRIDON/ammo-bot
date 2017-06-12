# -*- coding: utf-8 -*-
from __init__ import *
import telebot
from telebot import types
from botConstructor import BotConstructor

bot = telebot.TeleBot(API_TOKEN)
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


@bot.callback_query_handler(func=lambda call: call.data.find("top") != -1)
def callTop(call):
    botConstructor.botCallTop(call)

@bot.callback_query_handler(func=lambda call: call.data.find("discount") != -1)
def callDiscount(call):
    botConstructor.botCallDiscount(call)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        botConstructor.botSendMessage(message.chat.id, EMPTY_MESSAGE)
    except Exception as e:
        botConstructor.botSendMessage(message.chat.id, 'Opppsss!')
        print e

bot.polling()
