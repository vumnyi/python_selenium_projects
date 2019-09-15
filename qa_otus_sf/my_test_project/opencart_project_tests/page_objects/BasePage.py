from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by, selector)[index]

    def _click_ac(self, selector, index=0):
        # ac = Action Chains
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()
        return self

    def _click(self, selector, index=0):
        self.__element(selector, index).click()
        return self

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)
        return self

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(
            EC.visibility_of(self.__element(selector, index, link_text)))

    def _wait_for_clickable(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text
