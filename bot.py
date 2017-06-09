# -*- coding: utf-8 -*-
from __init__ import *
import telebot
from telebot import types
from parseData import IbisParseData

bot = telebot.TeleBot(API_TOKEN)
ibisParseData = IbisParseData()
calibersKeys = CALIBERS.keys()
discount = 0

def getKeyboards(array):
    markup = types.ReplyKeyboardMarkup(row_width=1)

    for key in array:
        markup.add(types.KeyboardButton(key))

    return markup

def getInlineKeyboards(array, callback='call'):
    markup = types.InlineKeyboardMarkup()

    for index, text in enumerate(array):
        key = types.InlineKeyboardButton(text=str(text), callback_data=callback + '_' + str(index))
        markup.add(key)

    return markup

def toSeconds(day):
    return day * 24 * 60 * 60

@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    with open("data/help.md", "r") as helpFile:
        helpText = helpFile.read()

        bot.send_message(message.chat.id, helpText, parse_mode="Markdown")

@bot.message_handler(commands=['discount'])
def sendDiscont(message):
    keyboard = getInlineKeyboards(DISCONT, 'discount')
    bot.send_message(message.chat.id, "Choose your discount:", reply_markup=keyboard)

@bot.message_handler(commands=['top'])
def sendTop(message):
    global discount
    discount = 0
    keyboard = getInlineKeyboards(calibersKeys, 'top')
    bot.send_message(message.chat.id, "Choose your caliber:", reply_markup=keyboard)

@bot.message_handler(commands=['median'])
def sendMedian(message):
    keyboard = getInlineKeyboards(calibersKeys, 'median')
    bot.send_message(message.chat.id, "Choose your caliber:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.find("top") != -1)
def callTop(call):
    global discount
    data = call.data.split('_')
    currentCaliber = calibersKeys[int(data[1])]
    visibleItems = 5
    
    ibisParseData.setCategoryId(currentCaliber)

    result = ibisParseData.topPrices(visibleItems, discount)

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, result, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.find("median") != -1)
def callMedian(call):
    data = call.data.split('_')
    currentCaliber = calibersKeys[int(data[1])]

    ibisParseData.setCategoryId(currentCaliber)
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "_%s %s_" % (ibisParseData.getMedian(), CURRENCY), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data.find("discount") != -1)
def callDiscount(call):
    data = call.data.split('_')
    global discount
    discount = DISCONT[int(data[1])]
    keyboard = getInlineKeyboards(calibersKeys, 'top')

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Choose your caliber:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    try:
        bot.send_message(message.chat.id, EMPTY_MESSAGE)
    except Exception as e:
        bot.send_message(message.chat.id, 'Opppsss!')
        print e

bot.polling()
