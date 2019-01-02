from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage

class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def go_to_gmail(self):
        self.driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en1')

    def autorization(self, email, password):
        lp = self.login_page
        lp.email_field.send_keys(email + Keys.ENTER)
        lp.password_field.send_keys(password + Keys.ENTER)
        assert lp.text_log_in == True

    def recovery_password(self, email):
        lp = self.login_page
        lp.email_field.send_keys(email + Keys.ENTER)
        lp.button_forgot_password.click()
        lp.account_recovery.send_keys('test')
        lp.button_next.click()
        lp.email_field.send_keys('test@test.com')
        lp.button_next.click()
        lp.any_email.send_keys('555555')
        lp.button_next.click()
        assert lp.text_wrong_code == True

    def switch_language(self):
        lp = self.login_page
        lp.button_language.click()
        lp.scroll_to_language.click()



