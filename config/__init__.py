import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

default_settings = {
    "API_TOKEN": apiKey["BOT_API_TOKEN"],
    "DEV": apiKey["DEV"],
    "DATA": {
        "DISCONT":  path + "/data/discount.vdb"
    },
    "TELEGRAM_BOT_NAME": '@ammoPriceBot',
    "DEFAULT_LANG": 'en', 
    "RESULT_ITEMS_COUNT": 20,
    "ALL_RESULT_ITEMS_COUNT": 26,
    "DISCONT": [0, 3, 5, 10, 15, 20, 25],
    "CURRENCY": "UAH",
    "CALIBERS": [
        "223_Rem",
        "308_Win",
        "338_Lapua_Mag",
        "7.62x39",
        "22_LR",
        "17_HMR",
        "30-06",
        "300_Win_Mag",
        "6.5_Creedmoor",
        "9x21",
        "22_WMR",
        "300_Win",
        "5.45x39",
        "7.62x54_R",
        "222_Rem",
        "9PA",
        "7mm_Rem_Mag",
        "338_Win_Mag",
        "12/70_bulet",
        "12/70_buckshot",
        "12/70_birdshot",
        "12/70",
        "12/76",
        "16/70",
        "20/70"
    ]
}


class Settings:
    def __init__(self):
        for key, value in default_settings.items():
            setattr(self, key, value)

settings = Settings()
