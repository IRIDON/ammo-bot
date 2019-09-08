# -*- coding: utf-8 -*-
from config import settings

result_count = settings.RESULT_ITEMS_COUNT
result_count_all = settings.ALL_RESULT_ITEMS_COUNT
bot_name = settings.TELEGRAM_BOT_NAME

message = {
 	"en": {
        "empy": "Sorry, but I don't know how to answer, plese run /help to find out the available commands.",
        "choose_caliber": "Choose your caliber:",
        "choose_caliber_with_shop": "Choose your caliber in the %s shop:",
        "choose_discount": "Choose your discount:",
        "choose_shop": "Choose shop:",
        "base_date": "Database update date",
        "link_text": "Visit site",
        "link_tmp": "Visit the %s",
        "base_error": "Database error, please try again.",
        "no_results": "Sorry, but this offer is not available, try to search the store site.",
        "discount_set": "Discount set!",
        "help": [
            "AmmoBot finds out the prices of ammo",
            "",
            u"/top - print the top %s offers with a low price" % (result_count),
            "/discount - set discount in stores",
            u"/all - print the top %s offers for all stores" % (result_count_all),
            "/start - start bot",
            "/help - print all commands",
            "",
            bot_name
        ]
    },
    "ru": {
        "empy": u"Извини, но я не знаю такой команды, пожалуйста запустите команду /help для поиска команды.",
        "choose_caliber": u"Выберите калибр:",
        "choose_caliber_with_shop": u"Выберите калибр из доступных в магазине %s:",
        "choose_discount": u"Выберите скидку:",
        "choose_shop": u"Выберите магазин:",
        "base_date": u"База обновлена",
        "link_text": u"Посетить сайт",
        "link_tmp": u"Посетить сайт %s",
        "base_error": u"Ошибка базы, пожалуйста попробуйте сделать ваш запрос позже.",
        "no_results": u"Извините, но запрашиваемые вами позиций нет в наличии в магазине, попробуйте перейти на сайт магазина и воспользоваться поиском.",
        "discount_set": u"Скидка установлена!",
        "help": [
            u"Патронобот узнает цены на патроны.",
            "",
            u"/top - вывести топ %s предложений с низкой ценой" % (result_count),
            "/discount - установить скидку в магазинах",
            u"/all - вывести топ %s предложений по всем магазинам" % (result_count_all),
            u"/start - старт бота",
            u"/help - вывести список доступных команд",
            "",
            bot_name
        ]
    },
    "uk": {
        "empy": u"Вибач, але я не знаю такої команди, будь ласка запустіть команду /help для пошуку команди.",
        "choose_caliber": u"Оберіть калібр:",
        "choose_caliber_with_shop": u"Оберіть калібр з доступних в магазині %s:",
        "choose_discount": u"Оберіть знижку:",
        "choose_shop": u"Оберіть магазин:",
        "base_date": u"База оновлена",
        "link_text": u"Відвідати сайт",
        "link_tmp": u"Відвідати сайт %s",
        "base_error": u"Помилка бази, будь ласка спробуйте зробити ваш запит пізніше.",
        "no_results": u"Вибачте, але запитувані вами позицій немає в наявності в магазині, спробуйте перейти на сайт магазину і скористатися пошуком.",
        "discount_set": u"Знижка встановлена!",
        "help": [
            u"Патронобот дізнається ціни на патрони.",
            "",
            u"/top - вивести топ %s пропозицій за ціною" % (result_count),
            u"/discount - встановити знижку в магазинах",
            u"/all - вивести топ %s пропозицій по всіх магазинах" % (result_count_all),
            u"/start - старт бота",
            u"/help - вивести список доступних команд",
            "",
            bot_name
        ]
    }
}
