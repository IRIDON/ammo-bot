from config import settings
from lib.ibisParse import IbisParseData
from lib.stvolParse import StvolParseData

parseIbis = IbisParseData(
    settings.SHOPS["ibis"]
)
parseStvol = StvolParseData(
    settings.SHOPS["stvol"]
)

parseIbis.parse()
parseStvol.parse()