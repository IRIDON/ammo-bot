from config import settings
from lib.Parse.ibisParse import IbisParseData
from lib.Parse.stvolParse import StvolParseData
from lib.Parse.safariParse import SafariParseData
from lib.Parse.kulyaParse import KulyaParseData

parseIbis = IbisParseData(
    settings.SHOPS["ibis"]
)
parseStvol = StvolParseData(
    settings.SHOPS["stvol"]
)
parseSafari = SafariParseData(
    settings.SHOPS["safari"]
)
kulyaParse = KulyaParseData(
    settings.SHOPS["kulya"]
)

parseIbis.parse()
parseStvol.parse()
parseSafari.parse()
kulyaParse.parse()
