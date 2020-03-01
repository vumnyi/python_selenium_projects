from api import _Api



class Api(_Api):

    def __init__(self):
        super().__init__('PrivatApi')

    def _update_rate(self, xrate):
        rate = self._get_private_rate(xrate.from_currency)
        return rate

    def _get_private_rate(self, from_currency):
        res = self._send_request('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11', method='get')
        res_json = res.json()
        self.log.debug(f'Private response: {res_json}')
        rate = self._find_rate(res_json, from_currency)

        return rate

    def _find_rate(self, response_data, from_currency):
        private_aliases_map = {840: 'USD', 1000: 'BTC'}
        if from_currency not in private_aliases_map:
            raise ValueError(f'Invalid from_currency: {from_currency}')

        currency_alias = private_aliases_map[from_currency]
        for e in response_data:
            if e['ccy'] == currency_alias:
                return float(e['sale'])
        raise ValueError(f'Invalid Privat response: {currency_alias} not found')
