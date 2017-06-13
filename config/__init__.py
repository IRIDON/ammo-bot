import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

default_settings = {
    "API_TOKEN": apiKey["BOT_API_TOKEN"],
    "BOTAN_API": apiKey["METRICA_KEY"],
    "BOT_HELP_FILE": path + "/data/help.md",
    "DATA_FILE": path + "/data/data.json",
    "AMMO_TYPE": {
        "rifle": "patrony-nareznye86",
        "pistol": "patrony-travmaticheskie",
        "bore_bulet": "puli-gladkostvolnie",
        "bore_buckshot": "kartechy",
        "bore_fraction": "droby"
    },
    "CALIBERS": {
        "223": ["198", "rifle"],
        "308": ["196", "rifle"],
        "338_Lapua_Mag": ["275", "rifle"],
        "300_Win_Mag": ["189", "rifle"],
        "30-06": ["177", "rifle"],
        "7.62x39": ["6476", "rifle"],
        "22LR": ["348", "rifle"],
        "9PA": ["8959", "pistol"],
        "12/70_bulet": ["364", "bore_bulet"],
        "12/70_buckshot": ["364", "bore_buckshot"],
        "12/70_fraction": ["364", "bore_fraction"]
    },
    "DISCONT": [0, 5, 10, 15, 20, 25],
    "CURRENCY": "UAH",
    "URL_TMP": "https://ibis.net.ua/products/%s/search/offset/?param_51[]=%s&isort=cheap&show_all=yes",
    "MESSAGE": {
        "empy": "Sorry, but I don't know how to answer, plese run /help to find out the available commands.",
        "choose_caliber": "Choose your caliber:",
        "choose_discount": "Choose your discount:"
    }
}