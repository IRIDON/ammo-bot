from config.shops import shops as SHOPS
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
# from lib.Parse.kulyaParse import KulyaParseData
from lib.Parse.shopGun import ShopGunData

parseIbis = IbisParseData(
    SHOPS["ibis"]
)
parseStvol = StvolParseData(
    SHOPS["stvol"]
)
parseSafari = SafariParseData(
    SHOPS["safari"]
)
# kulyaParse = KulyaParseData(
#     SHOPS["kulya"]
# )
shopgun = ShopGunData(
    SHOPS["shopgun"]
)

# kulyaParse.parse()
parseIbis.parse()
parseStvol.parse()
parseSafari.parse()
shopgun.parse()
