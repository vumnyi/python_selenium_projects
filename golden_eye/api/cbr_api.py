import requests

import xml.etree.ElementTree as ET

from api import _Api

class Api(_Api):
    def __init__(self):
        super().__init__('CBRApi')

    def _update_rate(self, xrate):
        rate = self._get_cbr_rate(xrate.from_currency)
        return rate

    def _get_cbr_rate(self, from_currency):
        res = self._send_request('http://www.cbr.ru/scripts/XML_daily.asp', method='get')
        self.log.debug(f'response.encoding: {res.encoding}')
        res_text = res.text
        self.log.debug(f'response.text: {res_text}')
        rate = self._find_rate(res_text, from_currency)

        return rate

    def _find_rate(self, response_text, from_currency):
        root = ET.fromstring(response_text)
        valutes = root.findall('Valute')

        cbr_valute_map = {840: 'USD'}
        currency_cbr_alias = cbr_valute_map[from_currency]

        for valute in valutes:
            if valute.find('CharCode').text == currency_cbr_alias:
                return float(valute.find('Value').text.replace(',', '.'))

        raise ValueError(f'Invalid CBR response: {from_currency} not found')