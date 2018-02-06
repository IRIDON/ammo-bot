import logging, os, sys
path = os.path.abspath(os.path.split(sys.argv[0])[0])
logPath = '%s/log/' % (path)

if not os.path.exists(logPath):
    os.makedirs(logPath)

logging.basicConfig(
    format = u'%(levelname)-8s [%(asctime)s] %(message)s',
    level = logging.ERROR,
    filename = '%s/log.log' % (logPath)
)

class Log():
    def error(self, data):
        logging.error(data)

    def info(self, data):
        logging.info(data)
