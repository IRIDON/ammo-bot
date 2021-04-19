import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

CALIBER_223REM = "223_Rem"
CALIBER_308WIN = "308_Win"
CALIBER_338LM = "338_Lapua_Mag"
CALIBER_762X39 = "7.62x39"
CALIBER_22LR = "22_LR"
CALIBER_17HMR = "17_HMR"
CALIBER_3006 = "30-06"
CALIBER_300WM = "300_Win_Mag"
CALIBER_65C = "6.5_Creedmoor"
CALIBER_300ACC = "300_AAC"
CALIBER_921 = "9x21"
CALIBER_22WNR = "22_WMR"
CALIBER_300WIN = "300_Win"
CALIBER_545X39 = "5.45x39"
CALIBER_762X54R = "7.62x54_R"
CALIBER_8X57JS = "8x57_JS"
CALIBER_222REM = "222_Rem"
CALIBER_9RA = "9RA"
CALIBER_7REMMAG = "7mm_Rem_Mag"
CALIBER_1270 = "12/70"
CALIBER_1276 = "12/76"
CALIBER_1670 = "16/70"
CALIBER_2070 = "20/70"

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
        CALIBER_223REM,
        CALIBER_308WIN,
        CALIBER_338LM,
        CALIBER_762X39,
        CALIBER_22LR,
        CALIBER_17HMR,
        CALIBER_3006,
        CALIBER_300WM,
        CALIBER_65C,
        CALIBER_300ACC,
        CALIBER_921,
        CALIBER_22WNR,
        CALIBER_300WIN,
        CALIBER_545X39,
        CALIBER_762X54R,
        CALIBER_8X57JS,
        CALIBER_222REM,
        CALIBER_9RA,
        CALIBER_7REMMAG,
        CALIBER_1270,
        CALIBER_1276,
        CALIBER_1670,
        CALIBER_2070,
    ]
}


class Settings:
    def __init__(self):
        for key, value in default_settings.items():
            setattr(self, key, value)

settings = Settings()
