from config import settings
from lib.ibisParse import IbisParseData
from lib.stvolParse import StvolParseData

parseData = IbisParseData(
    settings.SHOPS["ibis"]
)
parseData.parse()

parseStvol = StvolParseData(
    settings.SHOPS["stvol"]
)
parseStvol.parse()