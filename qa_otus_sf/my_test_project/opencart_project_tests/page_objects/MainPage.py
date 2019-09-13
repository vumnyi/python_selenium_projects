from locators import Main
from .BasePage import BasePage


class MainPage(BasePage):

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.driver.find_elements_by_xpath(Main.Featured.products['xpath'])[index]
        product_name = feature_product.find_element_by_xpath(Main.Featured.names['xpath']).text
        feature_product.click()
        return product_name
