import logging

logging.basicConfig(
    format = u'%(levelname)-8s [%(asctime)s] %(message)s',
    level = logging.ERROR,
    filename = u'log/log.log'
)

log = logging