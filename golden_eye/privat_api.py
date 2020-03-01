import requests

from models import XRate, peewee_datetime

from config import logging, LOGGER_CONFIG


log = logging.getLogger('PrivatApi')
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
    xrate.rate = get_private_rate(from_currency)
    # обновление поля updated
    xrate.updated = peewee_datetime.datetime.now()
    xrate.save()

    log.debug(f'rate after: {xrate}')
    log.info(f'Finished update for: {from_currency} => {to_currency}')

def get_private_rate(from_currency):
    res = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    res_json = res.json()
    log.debug(f'Private response: {res_json}')
    usd_rate = find_usd_rate(res_json)

    return usd_rate

def find_usd_rate(response_data):
    for e in response_data:
        if e['ccy'] == 'USD':
            return float(e['sale'])

    raise ValueError('Invalid Privat response: USD not found')