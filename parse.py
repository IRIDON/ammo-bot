from config import settings
from lib.ibisParse import IbisParseData
from lib.stvolParse import StvolParseData
from lib.safariParse import SafariParseData

parseIbis = IbisParseData(
    settings.SHOPS["ibis"]
)
parseStvol = StvolParseData(
    settings.SHOPS["stvol"]
)
parseSafari = SafariParseData(
    settings.SHOPS["safari"]
)

parseIbis.parse()
parseStvol.parse()
parseSafari.parse()
