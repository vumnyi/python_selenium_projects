from locators import Cart
class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_button_name(self, btn_name):
        self.driver.find_element_by_xpath(Cart.bottom_btn.button_name(btn_name)).click()

    def verify_product(self, name):
        self.driver.find_element_by_link_text(name)
