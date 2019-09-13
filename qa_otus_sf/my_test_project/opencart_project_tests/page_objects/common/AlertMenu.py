from locators import Common


class AlertDialog:

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element_by_xpath(Common.Alert.Success.link_to_login['xpath']).click()

    def click_to_cart(self):
        self.driver.find_element_by_xpath(Common.Alert.Success.link_to_cart['xpath']).click()

    def click_create_account(self):
        self.driver.find_element_by_xpath(Common.Alert.Success.link_to_create_account['xpath']).click()

    def click_link_product(self):
        self.driver.find_element_by_xpath(Common.Alert.Success.link_to_product['xpath']).click()

    def click_to_wish_list(self):
        self.driver.find_element_by_xpath(Common.Alert.Success.link_to_wish_list['xpath']).click()