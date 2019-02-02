from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.action_chains import ActionChains


class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_shop(self, url):
        self.driver.get(url)

    def go_to_section(self, one, two):
        driver = self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('//span[text() = "%s"]' % one)).perform()  # наводим на раздел мышки, для появления еще одного окна
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text() = "%s"]' % two))).click()  # кликаем в появившемся окне на раздел

    def choice_brand(self, one, two, three):
        # передаем три бренда
        driver = self.driver
        driver.find_element_by_xpath('//label[text() = "%s"]' % one).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))  # ожидает пока пересчитает кол-во подходящих по параметрам
        driver.find_element_by_xpath('//label[text() = "%s"]' % two).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))
        driver.find_element_by_xpath('//label[text() = "%s"]' % three).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))

    def choice_price(self, min_price, max_price):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="minnum_45"]').send_keys(min_price)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))
        driver.find_element_by_xpath('//*[@id="maxnum_45"]').send_keys(max_price)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))

    def choice_display_size(self, *args):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="Attr_prof_5828"]//span[text() = "Еще"]').click() #  раскрываем список размеров дисплея
        for i in args:
            driver.find_element_by_xpath(".//*[@id='Attr_prof_5828']//label[text() = '%s']" % (i)).click() #  кликаем по ссылке конткретного дисплея, в переменную подставляется значение размера
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@id="count_item"]')))

    def button_show(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[text() = "Показать"]')))
        driver.find_element_by_xpath(".//*[@class='ModelFilter__NumModelBtn Page__ActiveButtonBg ModelFilter__GALink' and text() = 'Показать']").click()

    def sort(self, x):
        driver = self.driver
        driver.find_element_by_xpath('.//*[@class="PanelSetUp__SortBlock"]').click()
        if x == 'max':
            # если передано max - сортируем по цене, сначала дорогие
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[@class="PanelSetUp__SortBlock"]//li[3]'))).click()
        elif x == 'min':
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[@class="PanelSetUp__SortBlock"]//li[2]'))).click()

    def count(self):
        driver = self.driver
        # сохраняем и печатаем итоговое кол-во моделей
        count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[@class="PanelSetUp__CountBlockItem"]'))).get_attribute('textContent')  # парсим текст
        count = ''.join(re.findall('\d', count))  # вытаскиваем из него только цифры
        print('Товаров: ' + count)

    def parse_first_name(self):
        driver = self.driver
        name = driver.find_element_by_xpath('.//*[@class="ModelList__LinkModel"]/span[1]').get_attribute('textContent')  # сохраняем название первой модели
        return name

    def parse_last_name(self):
        driver = self.driver
        pagination_list = driver.find_elements_by_xpath('.//*[@class="Paging__PageLink "]')  # парсим элементы пагинации
        pagination_list[-1].click()  # кликаем на последнюю страницу
        names = driver.find_elements_by_xpath('.//*[@class="ModelList__LinkModel"]/span')  # парсим все элементы спан с текстом модели
        return names[-1].get_attribute('textContent')  # берем текст последней модели и возвращаем его














