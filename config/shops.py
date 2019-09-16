import os, sys

path = os.path.abspath(os.path.split(sys.argv[0])[0])

shops = {
	"ibis": {
        "shop_name": "ibis",
        "url": "https://ibis.net.ua/",
        "url_tmp": "https://ibis.net.ua/products/%s/search/%s/?isort=cheap&show_all=yes",
        "data_file": path + "/data/ibis.json",
        "ammo_type": {
            "rifle": "patrony-nareznye86",
            "traumatic": "patrony-travmaticheskie",
            "bore": "patrony-gladkostvoljnye85"
        },
        "category": {
            "223_Rem": ["223-rem-55645-9fv", "rifle", 0],
            "308_Win": ["308-win-76251", "rifle", 1],
            "338_Lapua_Mag": ["338-lapua-mag", "rifle", 2],
            "7.62x39": ["762h39", "rifle", 3],
            "22_LR": ["22-lr", "rifle", 4],
            "17_HMR": ["17-hmr", "rifle", 5],
            "30-06": ["177", "rifle", 6],
            "300_Win_Mag": ["300-win-mag-0e0", "rifle", 7],
            "6.5_Creedmoor": ["65-creedmoor", "rifle", 8],
            "22_WMR": ["22-wmr", "rifle", 11],
            "7.62x54_R": ["7h57-r", "rifle", 12],
            "222_Rem": ["222-rem", "rifle", 13],
            "243_Win": ["243-win", "rifle", 50],
            "9x21": ["9mm-9h21", "rifle", 51],
            "5.45x39": ["545h39", "rifle", 52],
            "6.5x55": ["65x55", "rifle", 53],
            "50_BMG": ["50-bmg", "rifle", 54],
            "7mm_Rem_Mag": ["7mm-rem-mag", "rifle", 55],
            "8x57_JS": ["8h57-js", "rifle", 60],
            "9.3x62": ["93h62", "rifle", 61],

            "9RA": ["9-mm_m16", "traumatic", 70],

            "12/70": ["1270", "bore", 80],
            "12/76": ["1276", "bore", 81],
            "16/70": ["1670", "bore", 82],
            "20/70": ["2070", "bore", 83]
        }
    },
    "stvol": {
        "shop_name": "stvol",
        "url": "https://stvol.ua",
        "url_tmp": "https://stvol.ua/catalog/%s/filter/%s/apply/?page_sort=price_asc",
        "data_file": path + "/data/stvol.json",
        "ammo_type": {
            "rifle": "patrony_nareznye",
            "bore": "patrony_gladkostvolnye",
            "traumatic": "patrony_travmaticheskogo_deystviya"
        },
        "category": {
            "223_Rem": ["kalibr-is-91bb3ef4-f38b-11e2-bd5e-1cc1de282c58", "rifle", 0],
            "308_Win": ["kalibr-is-99957513-f397-11e2-bd5e-1cc1de282c58", "rifle", 1],
            "338_Lapua_Mag": ["kalibr-is-ca7b6293-be7d-11e4-bddc-1cc1de282c58", "rifle", 2],
            "22_LR": ["kalibr-is-ada64ea2-f397-11e2-bd5e-1cc1de282c58", "rifle", 3],
            "17_HMR": ["kalibr-is-b522825f-f397-11e2-bd5e-1cc1de282c58", "rifle", 4],
            "30-06": ["kalibr-is-c20cd9bc-f397-11e2-bd5e-1cc1de282c58", "rifle", 5],
            "300_Win_Mag": ["kalibr-is-cf2df0be-f397-11e2-bd5e-1cc1de282c58", "rifle", 6],
            "338_Win_Mag": ["kalibr-is-f37388bc-bb65-11e4-8f94-1cc1de282c58", "rifle", 7],
            "6.5_Creedmoor": ["kalibr-is-7c63096b-6b9c-11e7-ab40-00155dfa860b", "rifle", 8],
            "7.62x39": ["kalibr-is-6ed3512f-f38b-11e2-bd5e-1cc1de282c58", "rifle", 9],
            "222_Rem": ["kalibr-is-619213a1-f397-11e2-bd5e-1cc1de282c58", "rifle", 10],
            "7.62x54R": ["kalibr-is-9a7138f2-b03a-11e4-bc08-1cc1de282c58", "rifle", 50],
            "9x21": ["kalibr-is-d6ac461a-d936-11e4-8e15-1cc1de282c58", "rifle", 51],
            "5.45x39": ["kalibr-is-4f22644d-be84-11e4-bddc-1cc1de282c58", "rifle", 52],
            "300_AAC": ["kalibr-is-b79860b6-1837-11e6-9b00-1cc1de282c58", "rifle", 53],
            "6.5x55": ["kalibr-is-68682503-f398-11e2-bd5e-1cc1de282c58", "rifle", 54],
            "7mm_Rem_Mag": ["kalibr-is-05d3a7d3-d94a-11e4-8e15-1cc1de282c58", "rifle", 55],
            "9.3x62": ["kalibr-is-247b80d0-f398-11e2-bd5e-1cc1de282c58", "rifle", 70],

            "9RA": ["kalibr-is-f5f0d571-640b-11e4-9e41-1cc1de282c58", "traumatic", 80],

            "12/70": ["kalibr-is-a45bde61-d219-11e4-8e15-1cc1de282c58", "bore", 90],
            "12/76": ["kalibr-is-5998ccc0-d90e-11e4-8e15-1cc1de282c58", "bore", 91],
            "16/70": ["kalibr-is-114c2f3e-d210-11e4-8e15-1cc1de282c58", "bore", 92],
            "20/70": ["kalibr-is-d44ea6b4-d204-11e4-8e15-1cc1de282c58", "bore", 93]
        }
    },
    "safari": {
        "shop_name": "safari",
        "url": "https://safari-ukraina.com/",
        "url_tmp": "https://safari-ukraina.com/%s=%s;sort=cheap/",
        "data_file": path + "/data/safari.json",
        "ammo_type": {
            "rifle": "nareznye-patrony/c269/kalibr-nareznoy",
            "bore": "gladkie-patrony/c281/kalibr-gladk1",
            "traumatic": "travmaticheskie-patrony/c176999/detail_11301"
        },
        "category": {
            "223_Rem": ["5456", "rifle", 0],
            "308_Win": ["5475", "rifle", 1],
            "22_LR": ["5451", "rifle", 2],
            "17_HMR": ["5448", "rifle", 3],
            "30-06": ["5466", "rifle", 4],
            "300_Win_Mag": ["5473", "rifle", 5],
            "6.5_Creedmoor": ["6535", "rifle", 6],
            "7.62x54_R": ["5534", "rifle", 7],
            "270_Win": ["5462", "rifle", 8],
            "280_Rem": ["5464", "rifle", 9],
            "30_R_Blaser": ["5465", "rifle", 10],
            "300_Wby_Mag": ["5471", "rifle", 11],
            "375_H_&_H_Mag": ["5485", "rifle", 12],
            "470_Nitro-Express": ["5506", "rifle", 50],
            "9mm": ["5547", "rifle", 51],
            "5.45x39": ["5525", "rifle", 52],
            "300_AAC": ["5472", "rifle", 53],
            "7mm_Rem_Mag": ["5536", "rifle", 54],
            "7x64": ["5541", "rifle", 55],
            "7x65_R": ["5542", "rifle", 56],
            "8x57_JRS": ["5543", "rifle", 60],
            "8x57_JS": ["5544", "rifle", 61],
            "9.3x74_R": ["5552", "rifle", 62],

            "9RA": ["5384", "traumatic", 70],

            "12/70": ["5371", "bore", 80],
            "12/76": ["5372", "bore", 81],
            "16/70": ["5375", "bore", 82],
            "20/70": ["5377", "bore", 83]
        }
    },
    "kulya": {
        "shop_name": "kulya",
        "url": "http://kulya.com.ua",
        "url_tmp": "http://kulya.com.ua/patrony/%s/%s/?sort=p.price&order=ASC&limit=100",
        "data_file": path + "/data/kulya.json",
        "ammo_type": {
            "rifle": "nareznye/kalibr-nareznoj-",
            "traumatic": "travmaticheskie/kalibr-travmat-",
            "bore_bulet": "gladkostvolnye/pulya/kalibr-gladkostvolnyj-",
            "bore_buckshot": "gladkostvolnye/kartech/kalibr-gladkostvolnyj-/",
            "bore_birdshot": "gladkostvolnye/drob/kalibr-gladkostvolnyj-"
        },
        "category": {
            "223_Rem": ["-223-rem", "rifle", 0],
            "308_Win": ["-308-win", "rifle", 1],
            "7.62x39": ["7-62x39", "rifle", 2],
            "22_LR": ["-22lr", "rifle", 3],
            "17_HMR": ["-17-hmr", "rifle", 3],
            "30-06": ["-30-06", "rifle", 4],
            "7.62x54_R": ["7-62x54-r", "rifle", 5],
            "9x21": ["9h21", "rifle", 6],
            "22_WMR": ["-22-wmr", "rifle", 50],
            "243_Win": ["-243-win", "rifle", 52],
            "5.45x39": ["5-45x39", "rifle", 53],
            "9.3x62": ["9-3x62", "rifle", 54],
            "300_AAC": ["300-aac-blackout", "rifle", 55],
            "300_Win_Mag": ["300winmag", "rifle", 56],
            "7mm_Rem_Mag": ["7mm-rem-mag", "rifle", 57],

            "12_buckshot": ["12-67/12-70", "bore_buckshot", 60],
            "12_birdshot": ["12-65/12-67/12-70/12-76", "bore_birdshot", 61],
            "12_bulet": ["12-65/12-67/12-70/12-76", "bore_bulet", 62],

            "9RA": ["9-mm", "traumatic", 70]
        }
    },
    "shopgun": {
        "shop_name": "shopgun",
        "url": "https://shopgun.com.ua",
        "url_tmp": "https://shopgun.com.ua/patrhone/%s/%s/?sort=p.price&order=ASC&limit=1002",
        "data_file": path + "/data/shopgun.json",
        "ammo_type": {
            "rifle": "narezhie-patrhone",
            "bore": "gladkostvolnye-patrhone",
            "traumatic": "travmaticheskie-patroni"
        },
        "category": {
            "223_Rem": ["223-rem", "rifle", 0],
            "308_Win": ["308-win", "rifle", 1],
            "7.62x39": ["762-na-39", "rifle", 3],
            "22_LR": ["22-lr", "rifle", 4],
            "30-06": ["patrhone-30-06", "rifle", 5],
            "243_Win": ["243-win", "rifle", 6],

            "12/70": ["patroni-12-calibra", "bore", 20],
            "16/70": ["patroni-16-calibra", "bore", 21],
            "20/70": ["patroni-18-calibra", "bore", 22],

            "9RA": ["kalibr_9h21/?attrb[13]=101", "traumatic", 30]
        }
    },
    "tactical-systems": {
        "shop_name": "tactical systems",
        "url": "https://tactical-systems.com.ua",
        "url_tmp": "https://tactical-systems.com.ua/%s/filter/kalibr=%s;sort_price=ASC&limit=100/",
        "data_file": path + "/data/ts.json",
        "ammo_type": {
            "rifle": "nareznye-boepripasy",
            "traumatic": "boepripasyi-neletalnogo-deystviya",
            "bore": "gladkostvolnye-boepripasy"
        },
        "category": {
            "223_Rem": ["22", "rifle", 0],
            "308_Win": ["27", "rifle", 1],
            "22_LR": ["24", "rifle", 2],
            "7.62x39": ["13", "rifle", 3],
            "5.45x39": ["32", "rifle", 4],
            "9x21": ["26", "rifle", 5],
            "9x19": ["4", "rifle", 6],
            "9x18": ["33", "rifle", 7],
            "338_Lapua_Mag": ["16", "rifle", 8],
            "375_Chey_Tac": ["19", "rifle", 9],
            "300_AAC": ["28,29s", "rifle", 10],

            "12/70": ["23,25", "bore", 20],
            "16/70": ["31", "bore", 21],

            "12_GA_traumatic": ["23", "traumatic", 30],
            "9RA": ["34", "traumatic", 31],
        }
    },
    "tactica": {
        "shop_name": "tactica",
        "url": "https://tactica.kiev.ua",
        "url_request": "https://tactica.kiev.ua/index.php?route=module/filter_products/getProductsByCategory",
        "url_tmp": "https://tactica.kiev.ua/shop_1/ammunition/%s/&p_val=[0:3]&a_val=[%s]&limit=100&sort=p.price&order=DESC&page=1",
        "data_file": path + "/data/tactica.json",
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
            "223_Rem": ["[33:.223%20Rem%20(5.56%D1%8545)]", "rifle", 0],
            "308_Win": ["[33:.308%20Win%20(7.62%D1%8551)]", "rifle", 1],
            "22_LR": ["[33:.22LR]", "rifle", 2],
            "7.62x39": ["[33:7.62x39]", "rifle", 3],
            "9x21": ["[33:9x21]", "rifle", 5],

            "12/70": ["[33:12/70]", "bore", 20],
            "16/70": ["[33:16/70]", "bore", 21],
            "20/70": ["[33:20/70]", "bore", 22],

            # "5.45x39": ["[33:5.45x39]", "rifle", 4],
            # "30-06": ["[33:.30-06%20Sprg%20(7.62%D1%8563)]", "rifle", 6],
            # "300_Win_Mag": ["[33:.300%20Win%20Mag]", "rifle", 7],
            # "300_AAC": ["[33:.300%20Whisper/Blackout%20(7.62%D1%8535)]", "rifle", 8],
            # "9x19": ["[33:9x19]", "rifle", 9],
            # "9x18": ["[33:9x18]", "rifle", 10],
        }
    },
    "four_seasons" : {
        "shop_name": "four seasons",
        "url": "http://gun.lviv.ua/",
        "url_tmp": "http://gun.lviv.ua/index.php/zbroya-i-komplektuyuchi/boieprypasy/%s---%s",
        "data_file": path + "/data/four.json",
        "ammo_type": {
            "rifle": "narizni-patrony",
            "bore_12": "hladkostvolni-patrony/12-kalibr",
            "bore_16": "hladkostvolni-patrony/16-kalibr",
            "bore_20": "hladkostvolni-patrony/20-kalibr",
        },
        "category": {
            "22_LR": [349, "rifle", 0],
            "308_Win": [105, "rifle", 1],
            "30-06": [273, "rifle", 2],
            "300_Win_Mag": [274, "rifle", 3],
            "8x57": [278, "rifle", 4],
            "22_WMR": [280, "rifle", 5],

            "12/70": [0, "bore_12", 10],
            "16/70": [0, "bore_16", 11],
            "20/70": [0, "bore_20", 12],
        }
    }
}