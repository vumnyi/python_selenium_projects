from locators import Product, Common
from .BasePage import BasePage


class ProductPage(BasePage):

    def add_to_wish_list(self):
        self._click_ac(Product.product_options_div_add_to_wish_list)
        return self

    def add_to_cart(self):
        self._click_ac(Product.available_options_add_to_cart_button)
        return self

    def get_h1_text(self):
        return self._get_element_text(Product.product_options_div_h1, 0)

    def how_much_items_input(self, qty):
        self._input(Product.available_options_qty_input, qty)
        return self

    def click_add_to_cart_btn(self):
        self._click_ac(Product.available_options_add_to_cart_button)
        return self

    def verify_add_to_cart_btn_clickable(self):
        self._wait_for_clickable(Product.available_options_add_to_cart_button)
        return self

    def get_price_text(self):
        return self._get_element_text(Product.product_options_div_h2_price, 0)
