from locators import Cart
from .BasePage import BasePage

class CartPage(BasePage):

    def click_button_name(self, btn_name):
        self._click(Cart.bottom_btn.button_name(btn_name))
        return self

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self
