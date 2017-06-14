from config import settings
# from lib.ibisParse import IbisParse
from lib.stvolParse import StvolParseData

# parseData = IbisParseData(
# 	settings.CALIBERS,
# 	settings.DATA_FILE,
# 	settings.AMMO_TYPE,
# 	settings.URL_TMP,
# )
# parseData.parse()

parseStvol = StvolParseData(
	settings.SHOPS["stvol"]
)
parseStvol.parse()