from config import settings
from lib.parseData import IbisParseData

parseData = IbisParseData(
	settings.CALIBERS,
	settings.DATA_FILE,
	settings.AMMO_TYPE,
	settings.URL_TMP,
)
parseData.parse()
