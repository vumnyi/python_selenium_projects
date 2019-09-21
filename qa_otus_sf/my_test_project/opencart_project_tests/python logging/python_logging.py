import logging

logging.basicConfig(filename='test.log', filemode='a', level=logging.INFO)
# создаём logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# создаем консольный handler и задаем уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# создаём formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# добавляем formatter в ch
ch.setFormatter(formatter)
# добавляем ch к logger
logger.addHandler(ch)

# пример
logger.info('TEXT message level INFO')
logger.debug('TEXT message level DEBUG')
logger.error('TEXT message level ERROR')
logger.critical('TEXT message level CRITICAL')
