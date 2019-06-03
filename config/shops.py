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
            "8x57_JS": ["8h57-js", "rifle", 70],
            "9.3x62": ["93h62", "rifle", 71],
            "9PA": ["9-mm_m16", "traumatic", 72],
            "12/70": ["1270", "bore", 73],
            "12/76": ["1276", "bore", 74],
            "16/70": ["1670", "bore", 75],
            "20/70": ["2070", "bore", 76]
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
            "9RA": ["kalibr-is-f5f0d571-640b-11e4-9e41-1cc1de282c58", "traumatic", 71],
            "12/70": ["kalibr-is-a45bde61-d219-11e4-8e15-1cc1de282c58", "bore", 72],
            "12/76": ["kalibr-is-5998ccc0-d90e-11e4-8e15-1cc1de282c58", "bore", 73],
            "16/70": ["kalibr-is-114c2f3e-d210-11e4-8e15-1cc1de282c58", "bore", 74],
            "20/70": ["kalibr-is-d44ea6b4-d204-11e4-8e15-1cc1de282c58", "bore", 75]
        }
    },
    "safari": {
        "shop_name": "safari",
        "url": "http://safari-ukraina.com",
        "url_tmp": "http://safari-ukraina.com/%s=%s;sort=cheap/",
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
            "300 AAC": ["5472", "rifle", 53],
            "7mm_Rem_Mag": ["5536", "rifle", 54],
            "7x64": ["5541", "rifle", 55],
            "7x65_R": ["5542", "rifle", 56],
            "8x57_JRS": ["5543", "rifle", 70],
            "8x57_JS": ["5544", "rifle", 71],
            "9.3x74_R": ["5552", "rifle", 72],
            "9RA": ["5384", "traumatic", 73],
            "12/70": ["5371", "bore", 74],
            "12/76": ["5372", "bore", 75],
            "16/70": ["5375", "bore", 76],
            "20/70": ["5377", "bore", 77]
        }
    },
    # "kulya": {
    #     "shop_name": "kulya",
    #     "url": "http://kulya.com.ua",
    #     "url_tmp": "http://kulya.com.ua/patrony/%s/%s/?imit=100",
    #     "data_file": path + "/data/kulya.json",
    #     "ammo_type": {
    #         "rifle": "nareznye/kalibr-nareznoj-",
    #         "traumatic": "patrony-travmaticheskie",
    #         "bore_bulet": "pulya",
    #         "bore_buckshot": "kartech",
    #         "bore_birdshot": "drob-dlya-ohoti"
    #     },
    #     "category": {
    #         "223_Rem": ["-223-rem", "rifle", 0],
    #         "308_Win": ["?custom_f_88[0]=2e3330382057696e", "rifle", 1],
    #         "7.62x39": ["?custom_f_88[0]=372e3632783339", "rifle", 2],
    #         "22_LR": ["?custom_f_88[0]=2e32324c52", "rifle", 3],
    #         "17_HMR": ["?custom_f_88[0]=2e313720484d52", "rifle", 3],
    #         "30-06": ["?custom_f_88[0]=2e33302d3036", "rifle", 4],
    #         "7.62x54_R": ["?custom_f_88[0]=372e36327835342052", "rifle", 5],
    #         "9x21": ["?custom_f_88[0]=3920d0bcd0bc202839d185323129", "rifle", 6],
    #         "22_WMR": ["?custom_f_88[0]=2e323220574d52", "rifle", 50],
    #         "300_Win": ["?custom_f_88[0]=2e3330302057696e", "rifle", 51],
    #         "243_Win": ["?custom_f_88[0]=2e3234332057696e", "rifle", 52],
    #         "5.45x39": ["?custom_f_88[0]=352c3435783339", "rifle", 53],
    #         "12/70_buckshot": ["?custom_f_71[0]=31322f3730", "bore_buckshot", 54],
    #         "12/70_birdshot": ["?custom_f_71[0]=31322f3730", "bore_birdshot", 55],
    #         "12/70_bulet": ["?custom_f_71[0]=31322f3730", "bore_bulet", 56],
    #         "9RA": ["", "traumatic", 57]
    #     }
    # },
    "shopgun": {
        "shop_name": "shopgun",
        "url": "https://shopgun.com.ua",
        "url_tmp": "https://shopgun.com.ua/patrhone/%s/%s/?sort=p.price&order=ASC&limit=1002",
        "data_file": path + "/data/shopgun.json",
        "ammo_type": {
            "rifle": "narezhie-patrhone",
            "bore": "gladkostvolnye-patrhone"
        },
        "category": {
            "223_Rem": ["223-rem", "rifle", 0],
            "308_Win": ["308-win", "rifle", 1],
            "7.62x39": ["762-na-39", "rifle", 3],
            "22_LR": ["22-lr", "rifle", 4],
            "30-06": ["patrhone-30-06", "rifle", 5],
            "243_Win": ["243-win", "rifle", 50],
            "12_GA": ["patroni-12-calibra", "bore", 90],
            "16_GA": ["patroni-16-calibra", "bore", 91],
            "20_GA": ["patroni-18-calibra", "bore", 92]
        }
    },
    "tactical-systems": {
        "shop_name": "tactical systems",
        "url": "http://tactical-systems.com.ua",
        "url_tmp": "http://tactical-systems.com.ua/tovari/boepripasy/%s/?mfp=18-kalibr[%s]&sort=p.price&order=ASC&limit=100",
        "data_file": path + "/data/tactical-systems.json",
        "ammo_type": {
            "rifle": "nareznyie-boepripasyi",
            "bore": "gladkostvolnyie-boepripasyi"
        },
        "category": {
            "223_Rem": [".223%20Rem", "rifle", 0],
            
        }
    }
}