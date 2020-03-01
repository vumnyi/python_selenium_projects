import json
from unittest.mock import patch
from bs4 import BeautifulSoup

import pytest
import requests
import xmltodict

import models
import api


def get_privat_response(*args, **kwds):
    print('\nmocked method: get_privat_response')

    class Response:
        def __init__(self, response):
            self.text = json.dumps(response)

        def json(self):
            return json.loads(self.text)

    return Response([{'ccy': 'USD', 'base_ccy': 'UAH', 'sale': '30.0'}])


@pytest.fixture
def setup_db():
    models.init_db()


def test_privat_usd(setup_db):
    xrate = models.XRate.get(id=1)
    update_before = xrate.updated
    assert xrate.rate == 1.0
    api.update_rate(840, 980)
    xrate = models.XRate.get(id=1)
    update_after = xrate.updated
    assert xrate.rate > 24
    assert update_after > update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    assert api_log.response_text is not None

    assert '{"ccy":"USD","base_ccy":"UAH",' in api_log.response_text


def test_privat_btc(setup_db):
    xrate = models.XRate.get(from_currency=1000, to_currency=840)
    update_before = xrate.updated
    assert xrate.rate == 1.0

    api.update_rate(1000, 840)

    xrate = models.XRate.get(from_currency=1000, to_currency=840)
    update_after = xrate.updated

    assert xrate.rate > 5000
    assert update_after > update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'


def test_privat_currency_error(setup_db):
    xrate = models.XRate.get(id=1)
    assert xrate.rate == 1.0
    pytest.raises(ValueError, api.update_rate, 978, 980)


def test_cbr(setup_db):
    xrate = models.XRate.get(from_currency=840, to_currency=643)
    update_before = xrate.updated
    assert xrate.rate == 3
    api.update_rate(840, 643)
    xrate = models.XRate.get(from_currency=840, to_currency=643)
    update_after = xrate.updated
    assert xrate.rate > 60
    assert update_after > update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'http://www.cbr.ru/scripts/XML_daily.asp'
    assert api_log.response_text is not None

    assert '<NumCode>840</NumCode>' in api_log.response_text


@patch('api._Api._send', new=get_privat_response)
def test_privat_mock(setup_db):
    xrate = models.XRate.get(id=1)
    update_before = xrate.updated
    assert xrate.rate == 1.0

    api.update_rate(840, 980)
    xrate = models.XRate.get(id=1)
    update_after = xrate.updated

    assert xrate.rate == 30
    assert update_after > update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    assert api_log.response_text is not None

    assert '[{"ccy": "USD", "base_ccy": "UAH", "sale": "30.0"}]' in api_log.response_text


def test_api_error(setup_db):
    api.HTTP_TIMEOUT = 0.001
    xrate = models.XRate.get(id=1)
    update_before = xrate.updated
    assert xrate.rate == 1.0
    pytest.raises(requests.exceptions.RequestException, api.update_rate, 840, 980)

    xrate = models.XRate.get(id=1)
    update_after = xrate.updated

    assert xrate.rate == 1.0
    assert update_after == update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    assert api_log.response_text is None
    assert api_log.error is not None

    error_log = models.ErrorLog.select().order_by(models.ErrorLog.created.desc()).first()

    assert error_log is not None
    assert error_log.request_url == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    assert error_log.traceback is not None
    assert api_log.error == error_log.error
    assert 'Connection to api.privatbank.ua timed out' in error_log.error

    api.HTTP_TIMEOUT = 15


def test_cryptonator_rub(setup_db):
    from_currency = 1000
    to_currency = 643
    xrate = models.XRate.get(from_currency=from_currency, to_currency=to_currency)
    update_before = xrate.updated
    assert xrate.rate == 1.0

    api.update_rate(from_currency, to_currency)
    xrate = models.XRate.get(from_currency=from_currency, to_currency=to_currency)
    update_after = xrate.updated

    assert xrate.rate > 500000
    assert update_after > update_before

    api_log = models.ApiLog.select().order_by(models.ApiLog.created.desc()).first()

    assert api_log is not None
    assert api_log.request_url == 'https://api.cryptonator.com/api/ticker/btc-rub'
    assert api_log.response_text is not None

    assert '{"base":"BTC","target":"RUR","price":' in api_log.response_text


def test_xml_api():
    r = requests.get('http://localhost:5000/api/xrates/xml')
    assert '<xrates>' in r.text
    xml_rates = xmltodict.parse(r.text)
    assert 'xrates' in xml_rates
    assert isinstance(xml_rates['xrates']['xrate'], list)
    assert len(xml_rates['xrates']['xrate']) == 4


def test_json_api():
    r = requests.get('http://localhost:5000/api/xrates/json')
    json_rates = r.json()
    assert isinstance(json_rates, list)
    assert len(json_rates) == 4
    for rate in json_rates:
        assert 'from' in rate
        assert 'to' in rate
        assert 'rate' in rate


def test_json_api_rub():
    r = requests.get('http://localhost:5000/api/xrates/json?to_currency=643')
    json_rates = r.json()
    assert isinstance(json_rates, list)
    assert len(json_rates) == 2
    for rate in json_rates:
        assert 643 in rate.values()


def test_html_xrates():
    r = requests.get('http://localhost:5000/xrates')
    assert r.ok == True
    assert '<table border="1">' in r.text
    soup = BeautifulSoup(r.text, 'html.parser')
    assert soup.body is not None
    assert soup.table is not None
    assert len(soup.find('table').find_all_next('tr')) == 4
