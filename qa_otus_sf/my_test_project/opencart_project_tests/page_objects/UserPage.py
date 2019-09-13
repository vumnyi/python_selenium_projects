from locators import Common, Admin


class UserPage:
    def __init__(self, driver):
        self.driver = driver

    def login_user(self, email, password):
        browser = self.driver
        browser.find_element_by_xpath(Common.email_input['xpath']).send_keys(email)
        browser.find_element_by_xpath(Common.password_input['xpath']).send_keys(password)
        browser.find_element_by_xpath(Common.login_button['xpath']).click()

    def logout_user(self):
        browser = self.driver
        browser.find_element_by_xpath(Common.Header.my_account['xpath']).click()
        browser.find_element_by_xpath(Common.Header.my_account_dropdown('Logout')['xpath']).click()

    def open_right_menu_item(self, item_name):
        browser = self.driver
        browser.find_element_by_xpath(Admin.UserMenu.RightMenu.item(item_name)['xpath']).click()

    def verify_payment_form(self):
        self.driver.find_element_by_xpath(Admin.UserMenu.PaymentForm.it['xpath'])

    def verify_product(self, link_text):
        self.driver.find_element_by_link_text(link_text)
