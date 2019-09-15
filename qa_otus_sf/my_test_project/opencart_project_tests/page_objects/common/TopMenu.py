from locators import Common
from ..BasePage import BasePage

class TopMenu(BasePage):

    def change_currency(self, currency):
        if currency == 'euro':
            return self._click_ac(Common.Header.currency)._click(Common.Header.currency_euro)
        elif currency == 'sterling':
            return self._click_ac(Common.Header.currency)._click(Common.Header.currency_pound_sterling)
        elif currency == 'dollar':
            return self._click_ac(Common.Header.currency)._click(Common.Header.currency_dollar)
        return self
