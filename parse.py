from config.shops import shops as SHOPS
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
from lib.Parse.shopGunParse import ShopGunData
from lib.Parse.tacticalSystemsParse import TacticalSystemsParseData
from lib.Parse.kulyaParse import KulyaParseData
from lib.Parse.fourSeasonsParse import FourSeasonsParseData

models = [
	IbisParseData(SHOPS["ibis"]),
	StvolParseData(SHOPS["stvol"]),
	SafariParseData(SHOPS["safari"]),
	ShopGunData(SHOPS["shopgun"]),
	TacticalSystemsParseData(SHOPS["tactical_systems"]),
	KulyaParseData(SHOPS["kulya"]),
	# FourSeasonsParseData(SHOPS["four_seasons"]),
]

for model in models:
	model.parse()
