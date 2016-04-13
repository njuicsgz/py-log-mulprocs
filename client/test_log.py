import logging, logging.handlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost',
                    logging.handlers.DEFAULT_TCP_LOGGING_PORT)
rootLogger.addHandler(socketHandler)

LOG = logging.getLogger('default')


while True:
    LOG.debug('Quick zephyrs blow, vexing daft Jim.')
    LOG.info('How quickly daft jumping zebras vex.')
    LOG.warning('Jail zesty vixen who grabbed pay from quack.')
    LOG.error('The five boxing wizards jump quickly.')
    LOG.critical('critical')
    import time
    time.sleep(1)