from locators import Common
from ..BasePage import BasePage


class YourStoreBlock(BasePage):

    def get_cart_button_text(self):
        return self._get_element_text(Common.shopping_cart_total, 0)

    def search_input_text_and_click(self, text):
        self._input(Common.input_search, text)
        self._click(Common.search_button)
        return self
