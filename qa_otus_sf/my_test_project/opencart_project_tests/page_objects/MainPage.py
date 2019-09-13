from locators import Main


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.driver.find_elements_by_xpath(Main.Featured.products)[index]
        product_name = feature_product.find_element_by_xpath(Main.Featured.names).text
        feature_product.click()
        return product_name
