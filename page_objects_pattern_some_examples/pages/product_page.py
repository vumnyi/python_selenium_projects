from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def assert_item_in_cart(self, item_name, item_price, link):
        assert f'{item_name} был добавлен в вашу корзину.' in self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text, f'"Строка {item_name} был добавлен в вашу корзину." не совпадает {self.browser.find_element(*ProductPageLocators.MESSAGE).text} на странице промо {link}'
        assert item_price in self.browser.find_element(*ProductPageLocators.BASKET_TEXT).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
