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
        return self._wait_for_clickable(Product.available_options_add_to_cart_button["xpath"])

    def get_price_text(self):
        return self._get_element_text(Product.product_options_div_h2_price, 0)

    def click_tab_item(self, tab_name):
        return self._click(Product.choose_product_tab(tab_name))

    def review_input(self, field, text):
        if field == 'name':
            return self._input(Product.write_review_name, text)
        elif field == 'review':
            return self._input(Product.write_review_textarea, text)
        return self

    def choose_product_rating(self, rating):
        return self._click(Product.choose_review_rating(rating))

    def get_alert_text(self):
        return self._get_element_text(Common.Alert.Success.it, 0)
