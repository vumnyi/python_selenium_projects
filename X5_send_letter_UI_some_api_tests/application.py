from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure


def find_text_area(aria_label_text):
    return f"//textarea[@aria-label = '{aria_label_text}']"


def find_text(text):
    return f"//*[text() = '{text}']"


class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_gmail(self):
        with allure.step('Перехожу на страницу https://accounts.google.com/signin'):
            self.driver.get('https://accounts.google.com/signin')
            return self

    def send_to_locator_value(self, locator, value):
        with allure.step(f'Ищу локатор {locator} и отправляю значение {value}'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.driver.find_element_by_xpath(locator).send_keys(value + Keys.ENTER)
            return self

    def send_letter(self, email, topic, body):
        with allure.step(f'Отправляю письмо на поту {email} с темой {topic} и телос сообщения {body}'):
            self.driver.find_element_by_xpath(find_text('Написать')).click()
            self.driver.find_element_by_xpath(find_text_area('Кому')).send_keys(email)
            self.driver.find_element_by_xpath(find_text_area('Тема')).send_keys(topic)
            self.driver.find_element_by_xpath(find_text_area('Тело письма')).send_keys(body)
            self.driver.find_element_by_xpath(find_text('Отправить')).click()

    def click_by_locator(self, locator):
        with allure.step(f'Кликаю по локатору {locator}'):
            self.driver.find_element_by_xpath(locator).click()
            return self
