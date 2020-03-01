import logging

DB_NAME = 'golden-eye.db'

LOGGER_CONFIG = dict(level=logging.DEBUG,
                     file='api.log',
                     formatter=logging.Formatter('%(asctime)s [%(levelname)s] - %(name)s:%(message)s'))

HTTP_TIMEOUT = 15

IP_LIST = ['127.5.0.1']
