import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

default_settings = {
    "API_TOKEN": apiKey["BOT_API_TOKEN"],
    "BOTAN_API": apiKey["METRICA_KEY"],
    "BOT_HELP_FILE": path + "/data/help.md",
    "SHOPS": {
        "ibis": {
            "shop_name": "ibis",
            "url": "https://ibis.net.ua/",
            "url_tmp": "https://ibis.net.ua/products/%s/search/offset/?param_51[]=%s&isort=cheap&show_all=yes",
            "data_file": path + "/data/ibis.json",
            "ammo_type": {
                "rifle": "patrony-nareznye86",
                "pistol": "patrony-travmaticheskie",
                "bore_bulet": "puli-gladkostvolnie",
                "bore_buckshot": "kartechy",
                "bore_fraction": "droby"
            },
            "category": {
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
            }
        },
        "stvol": {
            "shop_name": "stvol",
            "url": "http://stvol.ua/",
            "url_tmp": "http://stvol.ua/catalog/%s",
            "data_file": path + "/data/stvol.json",
            "category": [
                "patrony_nareznye",
                "patrony_gladkostvolnye",
                "patrony_travmaticheskogo_deystviya"
            ],
            "ammo": {
                "223Rem": ["rifle"],
                "308Win": ["rifle"],
                "338_Lapua_Mag": ["rifle"],
                "300WM": ["rifle"],
                "30-06": ["rifle"],

                "22LR": ["rifle"],

                "12": ["bore_bulet"],
                "12/70": ["bore_buckshot"]
            }
        }
    },
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
    "DISCONT": [0, 3, 5, 10, 15, 20, 25],
    "CURRENCY": "UAH",
    "URL_TMP": "https://ibis.net.ua/products/%s/search/offset/?param_51[]=%s&isort=cheap&show_all=yes",
    "MESSAGE": {
        "empy": "Sorry, but I don't know how to answer, plese run /help to find out the available commands.",
        "choose_caliber": "Choose your caliber:",
        "choose_discount": "Choose your discount:",
        "base_date": "Database update date",
        "link_text": "Visit to site",
        "base_error": "Database error, please try again."
    }
}

class Settings:
    def __init__(self):
        for key, value in default_settings.items():
            setattr(self, key, value)

settings = Settings()
