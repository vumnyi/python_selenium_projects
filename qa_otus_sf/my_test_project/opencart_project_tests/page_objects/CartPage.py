from locators import Cart, Common
from .BasePage import BasePage

class CartPage(BasePage):

    def click_button_checkout(self):
        return self._click_ac(Common.Header.checkout)

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
