from config.shops import shops as SHOPS
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
from lib.Parse.shopGunParse import ShopGunData
from lib.Parse.tacticalSystemsParse import TacticalSystemsParseData

models = [
	IbisParseData(SHOPS["ibis"]),
	StvolParseData(SHOPS["stvol"]),
	SafariParseData(SHOPS["safari"]),
	ShopGunData(SHOPS["shopgun"]),
	TacticalSystemsParseData(SHOPS["ts"]),
]

for model in models:
	model.parse()
