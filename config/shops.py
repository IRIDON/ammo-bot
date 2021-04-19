import os, sys

from config import CALIBER_223REM, CALIBER_308WIN, CALIBER_338LM, CALIBER_762X39, CALIBER_22LR, CALIBER_17HMR, CALIBER_3006, CALIBER_300WM, CALIBER_65C, CALIBER_300ACC, CALIBER_921, CALIBER_22WNR, CALIBER_300WIN, CALIBER_545X39, CALIBER_762X54R, CALIBER_8X57JS, CALIBER_222REM, CALIBER_9RA, CALIBER_7REMMAG, CALIBER_1270, CALIBER_1276, CALIBER_1670, CALIBER_2070

path = os.path.abspath(os.path.split(sys.argv[0])[0])
data_path = path + "/data/"

shops = {
    "ibis": {
        "shop_name": "ibis",
        "url": "https://ibis.net.ua/",
        "url_tmp": "https://ibis.net.ua/products/%s/search/%s/?isort=cheap&category_view=0&show_all=yes",
        "data_file": data_path + "ibis.json",
        "ammo_type": {
            "rifle": "patrony-nareznye86",
            "traumatic": "patrony-travmaticheskie",
            "bore": "patrony-gladkostvoljnye85",
            "flober": "patrony-flobera",
        },
        "category": {
            CALIBER_223REM: ["223-rem-sw8", "rifle", 0],
            CALIBER_308WIN: ["308-win-dgs", "rifle", 1],
            CALIBER_921: ["9mm-9x21", "rifle", 51],
            CALIBER_762X39: ["762h39", "rifle", 3],
            CALIBER_22LR: ["22-lr_snw", "rifle", 4],
            CALIBER_17HMR: ["17-hmr_e94", "rifle", 5],
            CALIBER_338LM: ["338-lapua-mag-1s0", "rifle", 2],
            CALIBER_3006: ["30-06-s8e", "rifle", 6],
            CALIBER_65C: ["65-creedmoor", "rifle", 8],
            CALIBER_300ACC: ["300-whisperblackout", "rifle", 9],
            CALIBER_762X54R: ["762h54-r", "rifle", 12],
            CALIBER_8X57JS: ["8h57-js", "rifle", 60],
            CALIBER_22WNR: ["22-wmr_tgr", "rifle", 11],
            CALIBER_222REM: ["222-rem-99s", "rifle", 13],
            CALIBER_545X39: ["545h39", "rifle", 52],
            CALIBER_300WM: ["300-win-mag-0e0", "rifle", 7],
            CALIBER_7REMMAG: ["7mm-rem-mag", "rifle", 55],
            "243_Win": ["243-win-1i9", "rifle", 50],
            "50_BMG": ["50-bmg", "rifle", 54],
            "9.3x62": ["93h62", "rifle", 61],

            CALIBER_9RA: ["9-mm_m16/9-mm-ra", "traumatic", 70],

            CALIBER_1270: ["1270", "bore", 80],
            CALIBER_1276: ["1276", "bore", 81],
            CALIBER_1670: ["1670", "bore", 82],
            CALIBER_2070: ["2070", "bore", 83],
        }
    },
    "stvol": {
        "shop_name": "stvol",
        "url": "https://stvol.ua",
        "url_tmp": "https://stvol.ua/catalog/%s/filter/kalibr-is-%s/apply/?page_sort=price_asc",
        "data_file": data_path + "stvol.json",
        "ammo_type": {
            "rifle": "patrony_nareznye",
            "bore": "patrony_gladkostvolnye",
            "traumatic": "patrony_travmaticheskogo_deystviya"
        },
        "category": {
            CALIBER_223REM: ["91bb3ef4-f38b-11e2-bd5e-1cc1de282c58", "rifle", 0],
            CALIBER_308WIN: ["99957513-f397-11e2-bd5e-1cc1de282c58", "rifle", 1],
            CALIBER_338LM: ["ca7b6293-be7d-11e4-bddc-1cc1de282c58", "rifle", 2],
            CALIBER_22LR: ["ada64ea2-f397-11e2-bd5e-1cc1de282c58", "rifle", 3],
            CALIBER_17HMR: ["b522825f-f397-11e2-bd5e-1cc1de282c58", "rifle", 4],
            CALIBER_3006: ["c20cd9bc-f397-11e2-bd5e-1cc1de282c58", "rifle", 5],
            CALIBER_300WM: ["cf2df0be-f397-11e2-bd5e-1cc1de282c58", "rifle", 6],
            CALIBER_65C: ["7c63096b-6b9c-11e7-ab40-00155dfa860b", "rifle", 8],
            CALIBER_762X39: ["6ed3512f-f38b-11e2-bd5e-1cc1de282c58", "rifle", 9],
            CALIBER_222REM: ["619213a1-f397-11e2-bd5e-1cc1de282c58", "rifle", 10],
            CALIBER_762X54R: ["kalibr-is-9a7138f2-b03a-11e4-bc08-1cc1de282c58", "rifle", 50],
            CALIBER_921: ["d6ac461a-d936-11e4-8e15-1cc1de282c58", "rifle", 51],
            CALIBER_545X39: ["4f22644d-be84-11e4-bddc-1cc1de282c58", "rifle", 52],
            CALIBER_7REMMAG: ["05d3a7d3-d94a-11e4-8e15-1cc1de282c58", "rifle", 55],
            CALIBER_300ACC: ["b79860b6-1837-11e6-9b00-1cc1de282c58", "rifle", 53],
            CALIBER_8X57JS: ["kalibr-is-bd7a32ad-f398-11e2-bd5e-1cc1de282c58", "rifle", 71],
            "338_Win_Mag": ["f37388bc-bb65-11e4-8f94-1cc1de282c58", "rifle", 7],
            "6.5x55": ["68682503-f398-11e2-bd5e-1cc1de282c58", "rifle", 54],
            "9.3x62": ["247b80d0-f398-11e2-bd5e-1cc1de282c58", "rifle", 70],

            CALIBER_9RA: ["f5f0d571-640b-11e4-9e41-1cc1de282c58", "traumatic", 80],

            CALIBER_1270: ["a45bde61-d219-11e4-8e15-1cc1de282c58", "bore", 90],
            CALIBER_1276: ["5998ccc0-d90e-11e4-8e15-1cc1de282c58", "bore", 91],
            CALIBER_1670: ["114c2f3e-d210-11e4-8e15-1cc1de282c58", "bore", 92],
            CALIBER_2070: ["d44ea6b4-d204-11e4-8e15-1cc1de282c58", "bore", 93]
        }
    },
    "safari": {
        "shop_name": "safari",
        "url": "https://safari-ukraina.com/",
        "url_tmp": "https://safari-ukraina.com/%s=%s;sort=cheap/",
        "data_file": data_path + "safari.json",
        "ammo_type": {
            "rifle": "nareznye-patrony/c269/kalibr-nareznoy",
            "bore": "gladkie-patrony/c281/kalibr-gladk1",
            "traumatic": "travmaticheskie-patrony/c176999/detail_11301",
            "flober": "patrony-flobera/c178839"
        },
        "category": {
            CALIBER_223REM: ["5456", "rifle", 0],
            CALIBER_308WIN: ["5475", "rifle", 1],
            CALIBER_22LR: ["5451", "rifle", 2],
            CALIBER_17HMR: ["5448", "rifle", 3],
            CALIBER_3006: ["5466", "rifle", 4],
            CALIBER_300WM: ["5473", "rifle", 5],
            CALIBER_65C: ["6535", "rifle", 6],
            CALIBER_300ACC: ["5472", "rifle", 53],
            CALIBER_762X54R: ["5534", "rifle", 7],
            CALIBER_8X57JS: ["5544", "rifle", 61],
            CALIBER_545X39: ["5525", "rifle", 52],
            CALIBER_7REMMAG: ["5536", "rifle", 54],
            "270_Win": ["5462", "rifle", 8],
            "280_Rem": ["5464", "rifle", 9],
            "30_R_Blaser": ["5465", "rifle", 10],
            "300_Wby_Mag": ["5471", "rifle", 11],
            "375_H_&_H_Mag": ["5485", "rifle", 12],
            "470_Nitro-Express": ["5506", "rifle", 50],
            "9mm": ["5547", "rifle", 51],
            "7x64": ["5541", "rifle", 55],
            "7x65_R": ["5542", "rifle", 56],
            "8x57_JRS": ["5543", "rifle", 60],
            "9.3x74_R": ["5552", "rifle", 62],

            CALIBER_9RA: ["5384", "traumatic", 70],

            CALIBER_1270: ["5371", "bore", 80],
            CALIBER_1276: ["5372", "bore", 81],
            CALIBER_1670: ["5375", "bore", 82],
            CALIBER_2070: ["5377", "bore", 83],
        }
    },
    "kulya": {
        "shop_name": "kulya",
        "url": "http://kulya.com.ua",
        "url_tmp": "http://kulya.com.ua/patrony/%s/%s/?sort=p.price&order=ASC&limit=100",
        "data_file": data_path + "kulya.json",
        "ammo_type": {
            "rifle": "nareznye/kalibr-nareznoj-",
            "traumatic": "travmaticheskie/kalibr-travmat-",
            "bore_bulet": "gladkostvolnye/pulya/kalibr-gladkostvolnyj-",
            "bore_buckshot": "gladkostvolnye/kartech/kalibr-gladkostvolnyj-/",
            "bore_birdshot": "gladkostvolnye/drob/kalibr-gladkostvolnyj-"
        },
        "category": {
            CALIBER_223REM: ["-223-rem", "rifle", 0],
            CALIBER_308WIN: ["-308-win", "rifle", 1],
            CALIBER_762X39: ["7-62x39", "rifle", 2],
            CALIBER_22LR: ["-22lr", "rifle", 3],
            CALIBER_17HMR: ["-17-hmr", "rifle", 3],
            CALIBER_3006: ["-30-06", "rifle", 4],
            CALIBER_762X54R: ["7-62x54-r", "rifle", 5],
            CALIBER_921: ["9h21", "rifle", 6],
            CALIBER_22WNR: ["-22-wmr", "rifle", 50],
            CALIBER_300ACC: ["300-aac-blackout", "rifle", 55],
            CALIBER_300WM: ["300winmag", "rifle", 56],
            CALIBER_7REMMAG: ["7mm-rem-mag", "rifle", 57],
            CALIBER_545X39: ["5-45x39", "rifle", 53],
            "243_Win": ["-243-win", "rifle", 52],
            "9.3x62": ["9-3x62", "rifle", 54],

            "12_buckshot": ["12-67/12-70", "bore_buckshot", 60],
            "12_birdshot": ["12-65/12-67/12-70/12-76", "bore_birdshot", 61],
            "12_bulet": ["12-65/12-67/12-70/12-76", "bore_bulet", 62],

            CALIBER_9RA: ["9-mm", "traumatic", 70]
        }
    },
    "shopgun": {
        "shop_name": "shopgun",
        "url": "https://shopgun.com.ua",
        "url_tmp": "https://shopgun.com.ua/patrhone/%s/%s/?sort=p.price&order=ASC&limit=1002",
        "data_file": data_path + "shopgun.json",
        "ammo_type": {
            "rifle": "narezhie-patrhone",
            "bore": "gladkostvolnye-patrhone",
            "traumatic": "travmaticheskie-patroni"
        },
        "category": {
            CALIBER_223REM: ["223-rem", "rifle", 0],
            CALIBER_308WIN: ["308-win", "rifle", 1],
            CALIBER_762X39: ["762-na-39", "rifle", 3],
            CALIBER_22LR: ["22-lr", "rifle", 4],
            CALIBER_3006: ["patrhone-30-06", "rifle", 5],
            CALIBER_8X57JS: ["kalibr_16-70", "rifle", 7],
            "243_Win": ["243-win", "rifle", 6],

            CALIBER_1270: ["patroni-12-calibra", "bore", 20],
            CALIBER_1670: ["patroni-16-calibra", "bore", 21],
            CALIBER_2070: ["patroni-18-calibra", "bore", 22],

            CALIBER_9RA: ["kalibr_9-mm-r-a-", "traumatic", 30]
        }
    },
    "tactical-systems": {
        "shop_name": "tactical systems",
        "url": "https://tactical-systems.com.ua",
        "url_tmp": "https://tactical-systems.com.ua/%s/filter/kalibr=%s;sort_price=ASC/",
        "data_file": data_path + "ts.json",
        "ammo_type": {
            "rifle": "nareznye-boepripasy",
            "traumatic": "boepripasyi-neletalnogo-deystviya",
            "bore": "gladkostvolnye-boepripasy"
        },
        "category": {
            CALIBER_223REM: ["22", "rifle", 0],
            CALIBER_308WIN: ["27", "rifle", 1],
            CALIBER_22LR: ["24", "rifle", 2],
            CALIBER_338LM: ["16", "rifle", 8],
            CALIBER_762X39: ["13", "rifle", 3],
            CALIBER_921: ["26", "rifle", 5],
            CALIBER_300ACC: ["28,29s", "rifle", 10],
            CALIBER_545X39: ["32", "rifle", 4],
            "9x19": ["4", "rifle", 6],
            "9x18": ["33", "rifle", 7],
            "375_Chey_Tac": ["19", "rifle", 9],

            CALIBER_1270: ["23,25", "bore", 20],
            CALIBER_1670: ["31", "bore", 21],

            "12_GA_traumatic": ["23", "traumatic", 30],
            CALIBER_9RA: ["34", "traumatic", 31],
        }
    },
    "tactica": {
        "shop_name": "tactica",
        "url": "https://tactica.kiev.ua",
        "url_request": "https://tactica.kiev.ua/index.php?route=module/filter_products/getProductsByCategory",
        "url_tmp": "https://tactica.kiev.ua/shop_1/ammunition/%s/&p_val=[0:3]&a_val=[%s]&limit=100&sort=p.price&order=DESC&page=1",
        "data_file": data_path + "tactica.json",
        "ammo_type": {
            "rifle": "threaded",
            "traumatic": "traumatic",
            "bore": "smoothbore"
        },
        "categories_compare": {
            "rifle": 69,
            "traumatic": 70,
            "bore": 68,
        },
        "category": {
            CALIBER_223REM: ["[33:.223%20Rem%20(5.56%D1%8545)]", "rifle", 0],
            CALIBER_308WIN: ["[33:.308%20Win%20(7.62%D1%8551)]", "rifle", 1],
            CALIBER_22LR: ["[33:.22LR]", "rifle", 2],
            CALIBER_762X39: ["[33:7.62x39]", "rifle", 3],
            CALIBER_921: ["[33:9x21]", "rifle", 5],
            CALIBER_3006: ["[33:.30-06%20Sprg%20(7.62%D1%8563)]", "rifle", 6],

            CALIBER_1270: ["[33:12/70]", "bore", 20],
            CALIBER_1670: ["[33:16/70]", "bore", 21],
            CALIBER_2070: ["[33:20/70]", "bore", 22],

            # CALIBER_545X39: ["[33:5.45x39]", "rifle", 4],
            # CALIBER_300WM: ["[33:.300%20Win%20Mag]", "rifle", 7],
            # CALIBER_300ACC: ["[33:.300%20Whisper/Blackout%20(7.62%D1%8535)]", "rifle", 8],
            # "9x19": ["[33:9x19]", "rifle", 9],
            # "9x18": ["[33:9x18]", "rifle", 10],
        }
    },
    "four-seasons" : {
        "shop_name": "four seasons",
        "url": "http://gun.lviv.ua/",
        "url_tmp": "http://gun.lviv.ua/index.php/zbroya-i-komplektuyuchi/boieprypasy/%s---%s",
        "data_file": data_path + "four.json",
        "ammo_type": {
            "rifle": "narizni-patrony",
            "bore_12": "hladkostvolni-patrony/12-kalibr",
            "bore_16": "hladkostvolni-patrony/16-kalibr",
            "bore_20": "hladkostvolni-patrony/20-kalibr",
        },
        "category": {
            CALIBER_22LR: [349, "rifle", 0],
            CALIBER_308WIN: [105, "rifle", 1],
            CALIBER_3006: [273, "rifle", 2],
            CALIBER_300WM: [274, "rifle", 3],
            CALIBER_8X57JS: [278, "rifle", 4],
            CALIBER_22WNR: [280, "rifle", 5],

            CALIBER_1270: [0, "bore_12", 10],
            CALIBER_1670: [0, "bore_16", 11],
            CALIBER_2070: [0, "bore_20", 12],
        }
    }
}