from config.shops import shops as SHOPS

from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
from lib.Parse.shopGunParse import ShopGunData
from lib.Parse.tacticalSystemsParse import TacticalSystemsParseData
from lib.Parse.kulyaParse import KulyaParseData
from lib.Parse.fourSeasonsParse import FourSeasonsParseData
from lib.Parse.tacticaParse import TacticaParseData

from lib.Logger.logger import Log

log = Log()

models = [
	# IbisParseData(),
	# StvolParseData(),
	SafariParseData(),
	# ShopGunData(),
	# TacticalSystemsParseData(),
	# KulyaParseData(),
	# TacticaParseData(),
	# FourSeasonsParseData(),
]
for model in models:
	model.parse()
# try:
# 	for model in models:
# 		model.parse()
# except Exception as error:
#     log.error(error)