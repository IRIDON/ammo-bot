import os, sys
from key import default_api_key as apiKey

path = os.path.abspath(os.path.split(sys.argv[0])[0])

default_settings = {
    "API_TOKEN": apiKey["BOT_API_TOKEN"],
    "BOTAN_API": apiKey["METRICA_KEY"],
    "BOT_HELP_FILE": path + "/data/help.md",
    "AVAILABLE_SHOPS": [
        "ibis",
        "stvol",
        "safari"
    ],
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
                "22_WMR": ["358", "rifle"],
                "222_Rem": ["533", "rifle"],
                "22_LR": ["348", "rifle"],
                "243_Win": ["188", "rifle"],
                "223-Rem": ["198", "rifle"],
                "30-06": ["177", "rifle"],
                "308_Win": ["196", "rifle"],
                "300_Win_Mag": ["189", "rifle"],
                "338_Lapua_Mag": ["275", "rifle"],
                "6.5x55": ["6281", "rifle"],
                "7mm Rem Mag": ["197", "rifle"],
                "7.62x39": ["6476", "rifle"],
                "8x57_JS": ["6324", "rifle"],
                "9.3x62": ["944", "rifle"],
                "9PA": ["8959", "pistol"],
                "12/70_bulet": ["364", "bore_bulet"],
                "12/70_buckshot": ["364", "bore_buckshot"],
                "12/70_fraction": ["364", "bore_fraction"]
            }
        },
        "stvol": {
            "shop_name": "stvol",
            "url": "http://stvol.ua",
            "url_tmp": "http://stvol.ua/catalog/%s/filter/%s/apply/?page_sort=price_asc",
            "data_file": path + "/data/stvol.json",
            "ammo_type": {
                "rifle": "patrony_nareznye",
                "bore": "patrony_gladkostvolnye"
            },
            "category": {
                "222Rem": ["kalibr-is-619213a1-f397-11e2-bd5e-1cc1de282c58", "rifle"],
                "223Rem": ["kalibr-is-91bb3ef4-f38b-11e2-bd5e-1cc1de282c58", "rifle"],
                "22LR": ["kalibr-is-ada64ea2-f397-11e2-bd5e-1cc1de282c58", "rifle"],
                "30-06": ["kalibr-is-c20cd9bc-f397-11e2-bd5e-1cc1de282c58", "rifle"],
                "300WM": ["kalibr-is-cf2df0be-f397-11e2-bd5e-1cc1de282c58", "rifle"],
                "308Win": ["kalibr-is-99957513-f397-11e2-bd5e-1cc1de282c58", "rifle"],
                "338_Lapua Mag": ["kalibr-is-ca7b6293-be7d-11e4-bddc-1cc1de282c58", "rifle"],
                "338_Win_Mag": ["kalibr-is-f37388bc-bb65-11e4-8f94-1cc1de282c58", "rifle"],
                "6.5x55": ["kalibr-is-68682503-f398-11e2-bd5e-1cc1de282c58", "rifle"],
                "7.62x54R": ["kalibr-is-9a7138f2-b03a-11e4-bc08-1cc1de282c58", "rifle"],
                "7mm_Rem_Mag": ["kalibr-is-05d3a7d3-d94a-11e4-8e15-1cc1de282c58", "rifle"],
                "9.3x62": ["kalibr-is-247b80d0-f398-11e2-bd5e-1cc1de282c58", "rifle"],
                "12/70": ["kalibr-is-a45bde61-d219-11e4-8e15-1cc1de282c58", "bore"],
                "12/76": ["kalibr-is-5998ccc0-d90e-11e4-8e15-1cc1de282c58", "bore"],
                "16/70": ["kalibr-is-114c2f3e-d210-11e4-8e15-1cc1de282c58", "bore"],
                "20/70": ["kalibr-is-d44ea6b4-d204-11e4-8e15-1cc1de282c58", "bore"]
            }
        },
        "safari": {
            "shop_name": "safari",
            "url": "http://safari-ukraina.com",
            "url_tmp": "http://safari-ukraina.com/%s=%s;sort=cheap/",
            "data_file": path + "/data/safari.json",
            "ammo_type": {
                "rifle": "nareznye-patrony/c269/kalibr-nareznoy",
                "bore": "gladkie-patrony/c281/kalibr-gladk1"
            },
            "category": {
                "22_LR": ["5451", "rifle"],
                "223_Remington": ["5456", "rifle"],
                "270_Winchester": ["5462", "rifle"],
                "280_Remington": ["5464", "rifle"],
                "30_R_Blaser": ["5465", "rifle"],
                "30-06_Springfield": ["5466", "rifle"],
                "300_Weatherby_Magnum": ["5471", "rifle"],
                "300_Winchester_Magnum": ["5473", "rifle"],
                "308_Winchester": ["5475", "rifle"],
                "375_Holland_&_Holland_Magnum": ["5485", "rifle"],
                "470_Nitro-Express": ["5506", "rifle"],
                "7mm_Remington_Magnum": ["5536", "rifle"],
                "7x64": ["5541", "rifle"],
                "7x65_R": ["5542", "rifle"],
                "8x57_JRS": ["5543", "rifle"],
                "8x57_JS": ["5544", "rifle"],
                "9.3x74_R": ["5552", "rifle"],
                "12/70": ["5371", "bore"],
                "12/76": ["5372", "bore"],
                "16/70": ["5375", "bore"],
                "20/70": ["5377", "bore"]
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
