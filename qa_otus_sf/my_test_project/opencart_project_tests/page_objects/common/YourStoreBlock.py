from locators import Common
from ..BasePage import BasePage


class YourStore(BasePage):

    def get_cart_button_text(self):
        return self._get_element_text(Common.shopping_cart_total, 0)
