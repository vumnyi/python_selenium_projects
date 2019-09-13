from locators import Product, Common
from .BasePage import BasePage


class ProductPage(BasePage):

    def add_to_wish_list(self):
        self.driver.find_element_by_xpath(Product.product_options_div_add_to_wish_list['xpath']).click()
        
    def add_to_cart(self):
        self.driver.find_element_by_xpath(Product.available_options_add_to_cart_button['xpath']).click()
