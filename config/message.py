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
        "base_error": "Database error, please try again.\n Or, please tell me about it to iridon2@gmail.com",
        "no_results": "Sorry, but this offer is not available, try to search the store site.",
        "discount_set": "Discount set!",
        "help": [
            u"AmmoBot finds out the prices of ammo 🇺🇦",
            u"",
            u"/top - print the TOP %s from select shop" % (result_count),
            u"/discount - set discount in stores",
            u"/all - print the TOP %s offers for all stores" % (result_count_all),
            u"/start - start bot",
            u"/help - print all commands",
            u"",
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
        "base_error": u"Помилка бази, будь ласка спробуйте зробити ваш запит пізніше.\n Або, будь ласка повідомте мені про це iridon2@gmail.com",
        "no_results": u"Вибачте, але запитувані вами позицій немає в наявності в магазині, спробуйте перейти на сайт магазину і скористатися пошуком.",
        "discount_set": u"Знижка встановлена!",
        "help": [
            u"Патронобот дізнається ціни на патрони 🇺🇦",
            u"",
            u"/top - вивести ТОП %s по магазину" % (result_count),
            u"/discount - встановити знижку в магазинах",
            u"/all - вивести ТОП %s пропозицій по всіх магазинах" % (result_count_all),
            u"/start - старт бота",
            u"/help - вивести список доступних команд",
            u"",
            bot_name
        ]
    }
}
