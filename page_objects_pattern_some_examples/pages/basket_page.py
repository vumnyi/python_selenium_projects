from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_ITEMS), \
            "Items is presented, but should not be"

    def should_be_text_is_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), 'Should be text "Ваша корзина пуста"'
