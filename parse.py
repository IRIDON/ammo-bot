from config import settings
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData

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
