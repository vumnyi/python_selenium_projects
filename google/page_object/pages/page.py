from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_element_visible_xpath(self, path):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, path)))
        except WebDriverException:
            return False

    def is_element_visible_css(self, path):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, path)))
        except WebDriverException:
            return False

    def is_text_present(self, locator, text):
        try:
            return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, locator), text))
        except WebDriverException:
            return False

    def is_text_present_by_css(self, locator, text):
        try:
            return self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
        except WebDriverException:
            return False

