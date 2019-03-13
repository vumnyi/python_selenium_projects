from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)

    def login(self, email, password):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="login-image"]')))
        driver.find_element_by_xpath('//*[@name="mxEmail"]').send_keys(email)
        driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//option[@selected]')))
        if "GB" not in driver.find_element_by_xpath('//option[@selected]').get_attribute('textContent'):
            driver.find_element_by_xpath('//select').click()
            driver.find_element_by_xpath('//option[@value="string:en"]').click()

    def go_to_section(self, section):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[text() ="%s"]' % section))).click()

    def add_new_user(self, first_name, last_name, email, password, country, role, store_cluster, store):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text() ="Add new"]'))).click()
        driver.find_element_by_xpath('//*[@data-filter-key="fNameText"]//input').send_keys(first_name)
        driver.find_element_by_xpath('//*[@data-filter-key="lNameText"]//input').send_keys(last_name)
        driver.find_element_by_xpath('//*[@data-filter-key="email"]//input').send_keys(email)
        driver.find_element_by_xpath('//*[@data-filter-key="password"]//input').send_keys(password)
        driver.find_element_by_xpath('//*[@data-filter-key="countryId"]//input/following::div[1]').click()
        driver.find_element_by_xpath('//span[text() = "%s"]' % country).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text() = "%s"]' % country)))
        driver.find_element_by_xpath('//*[@data-filter-key="roleId"]//input/following::div[1]').click()
        driver.find_element_by_xpath('//span[text() = "%s"]' % role).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text() = "%s"]' % role)))
        driver.find_element_by_xpath('//*[@data-filter-key="storeClusterId"]//input/following::div[1]').click()
        driver.find_element_by_xpath('//li/span[text() = "%s"]' % store_cluster).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text() = "%s"]' % store_cluster)))
        driver.find_element_by_xpath('//*[@data-filter-key="storeId"]//input/following::div[1]').click()
        driver.find_element_by_xpath('//*[contains(text(),"%s")]' % store).click()
        driver.find_element_by_xpath('//*[@class="on-idle"]').click()
        try:
            driver.find_element_by_xpath('//button[text() = "Create"]').click()
        except:
            pass
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, '//span[text() = "Success"]')))


    def check_adding_user(self, first_name, last_name, email, country, role, store_cluster, store):
        driver = self.driver
        driver.find_element_by_xpath('//span[text() = "%s"]' % role).click()
        driver.find_element_by_xpath('//span[text() = "%s %s"]' % (first_name, last_name)).click()
        assert first_name in driver.find_element_by_xpath('//*[@data-filter-key="fNameText"]//input').get_attribute('value')
        assert last_name in driver.find_element_by_xpath('//*[@data-filter-key="lNameText"]//input').get_attribute('value')
        assert email in driver.find_element_by_xpath('//*[@data-filter-key="email"]//input').get_attribute('value')
        assert country in driver.find_element_by_xpath('//*[@data-filter-key="countryId"]//input/following::div[1]/span').get_attribute('textContent')
        assert role in driver.find_element_by_xpath('//*[@data-filter-key="roleId"]//input/following::div[1]/span').get_attribute('textContent')
        assert store_cluster in driver.find_element_by_xpath('//*[@data-filter-key="storeClusterId"]//input/following::div[1]/span').get_attribute('textContent')
        assert store in driver.find_element_by_xpath('//*[@data-filter-key="storeId"]//input/following::div[1]/span').get_attribute('textContent')

    def delete_user(self, first_name, last_name, role):
        driver = self.driver
        driver.get('https://dev.mercaux.com/#/en/users')
        driver.find_element_by_xpath('//span[text() = "%s"]' % role).click()
        driver.find_element_by_xpath('//span[text() = "%s %s"]' % (first_name, last_name)).click()
        # time.sleep(2)
        driver.find_element_by_xpath('//span[text() = "Delete"]').click()
        driver.find_element_by_xpath('//button[text() = "OK"]').click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[text() = "Success"]')))






