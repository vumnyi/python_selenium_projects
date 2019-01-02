from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_gmail(self):
        self.driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en1')

    def autorization(self, email, password):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#identifierId')))
        driver.find_element_by_css_selector('#identifierId').send_keys(email + Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))).send_keys(password + Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//h1'), 'Добро пожаловать'))

    def recovery_password(self, email):
        driver = self.driver
        driver.find_element_by_css_selector('#identifierId').send_keys(email + Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_css_selector('#forgotPassword').click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//h1'), "Account recovery"))
        driver.find_element_by_css_selector('input[name="password"]').send_keys('test')
        driver.find_element_by_xpath('//div//*[contains(text(), "Next")]').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#month'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="month"]/option[4]'))).click()
        driver.find_element_by_css_selector('#identifierId').send_keys('test@test.com')
        driver.find_element_by_css_selector('idvAnyEmailPin').send_keys('wrong code')

    def switch_language(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="MocG8c B9IrJb LMgvRb KKjvXb"]'))).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="OA0qNb ncFHed"]//*[contains(text(), "Русский")]')))
        element = driver.find_element_by_xpath('//*[@class="OA0qNb ncFHed"]//*[contains(text(), "Русский")]')
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()


