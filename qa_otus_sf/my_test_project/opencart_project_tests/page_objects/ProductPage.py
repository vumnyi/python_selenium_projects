from locators import Product, Common
from .BasePage import BasePage

class ProductPage(BasePage):

    def add_to_wish_list(self):
        self._click(Product.product_options_div_add_to_wish_list)

    def add_to_cart(self):
        self._click(Product.available_options_add_to_cart_button)