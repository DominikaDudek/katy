import logging

# create and configure logger

logging.basicConfig(filename='/Users/dominikadudek/Desktop/learn_some_python/socratica/example.log', level=logging.DEBUG)
logger = logging.getLogger()

logger.info('you are amazing')
