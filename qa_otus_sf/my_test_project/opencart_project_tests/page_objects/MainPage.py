from locators import Main
from .BasePage import BasePage


class MainPage(BasePage):

    def click_featured_product(self, number):
        index = number - 1
        self._click_ac(Main.Featured.products, index=index)

    def featured_product_name(self, number):
        index = number - 1
        return self._get_element_text(Main.Featured.names, index=index)

    def click_promoblock(self):
        self._click_ac(Main.promoblock)
