import requests

import xml.etree.ElementTree as ET

from models import XRate, peewee_datetime
from config import logging, LOGGER_CONFIG

log = logging.getLogger('CBRApi')
fh = logging.FileHandler(LOGGER_CONFIG['file'])
fh.setLevel(LOGGER_CONFIG['level'])
fh.setFormatter(LOGGER_CONFIG['formatter'])
log.addHandler(fh)
log.setLevel(LOGGER_CONFIG['level'])


def update_xrates(from_currency, to_currency):
    log.info(f'Started update for: {from_currency} => {to_currency}')
    # получение курса из БД
    xrate = XRate.select().where(XRate.from_currency == from_currency,
                                 XRate.to_currency == to_currency).first()
    log.debug(f'rate before: {xrate}')
    # получение нового значения от Привата и сохранение его в объект xrate
    xrate.rate = get_cbr_rate(from_currency)
    # обновление поля updated
    xrate.updated = peewee_datetime.datetime.now()
    xrate.save()

    log.debug(f'rate after: {xrate}')
    log.info(f'Finished update for: {from_currency} => {to_currency}')


def get_cbr_rate(from_currency):
    res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    log.debug(f'response.encoding: {res.encoding}')
    res_text = res.text
    log.debug(f'response.text: {res_text}')
    usd_rate = find_usd_rate(res_text)

    return usd_rate


def find_usd_rate(response_text):
    root = ET.fromstring(response_text)
    valutes = root.findall('Valute')

    for valute in valutes:
        if valute.find('CharCode').text == 'USD':
            return float(valute.find('Value').text.replace(',', '.'))

    raise ValueError('Invalid CBR response: USD not found')
