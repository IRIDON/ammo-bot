from config.shops import shops as SHOPS
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
from lib.Parse.shopGunParse import ShopGunData
from lib.Parse.tacticalSystemsParse import TacticalSystemsParseData

parseIbis = IbisParseData(
    SHOPS["ibis"]
)
parseStvol = StvolParseData(
    SHOPS["stvol"]
)
parseSafari = SafariParseData(
    SHOPS["safari"]
)
shopgun = ShopGunData(
    SHOPS["shopgun"]
)
tacticalSystems = TacticalSystemsParseData(
    SHOPS["tactical-systems"]
)


# parseIbis.parse()
# parseStvol.parse()
# parseSafari.parse()
# shopgun.parse()
tacticalSystems.parse()
