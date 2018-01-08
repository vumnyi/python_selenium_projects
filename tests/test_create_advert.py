import unittest
from selenium import webdriver
import time
import os




class all_in(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_create_advert(self):
        driver = self.driver
        driver.get("http://srv-site-dev/account/login")
        driver.find_element_by_xpath('//*[@id="Username"]').send_keys('7252395')
        driver.find_element_by_xpath('//*[@id="Password"]').send_keys('22061941')
        driver.find_element_by_xpath('/html/body/div[2]/main/section/section/form/div[2]/button').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/a[6]').click() # список объявлений
        driver.find_element_by_xpath('/html/body/div[1]/advert-list-admin/main/section/section/a').click() #добавить объявление
        driver.find_element_by_xpath('//*[@id="Manager_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Manager_chosen"]/div/ul/li[5]').click()
        driver.find_element_by_xpath('//*[@id="City_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="City_chosen"]/div/ul/li[10]').click()
        driver.find_element_by_xpath('//*[@id="Vin"]').send_keys('sdg345435435fdgdf')
        driver.find_element_by_xpath('//*[@id="VehicleType_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="VehicleType_chosen"]/div/ul/li[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="Brand_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Brand_chosen"]/div/ul/li[4]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="Model_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Model_chosen"]/div/ul/li[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="Modification_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Modification_chosen"]/div/ul/li[14]').click()
        driver.find_element_by_xpath('//*[@id="Option_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Option_chosen"]/div/ul/li[2]').click()
        driver.find_element_by_xpath('//*[@id="Price"]').send_keys('2860000')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #скрипт для прокрутки страницы вниз
        driver.find_element_by_xpath('//*[@id="Year_chosen"]/a').click()
        driver.find_element_by_xpath('//*[@id="Year_chosen"]/div/ul/li[3]').click()
        driver.find_element_by_xpath('//*[@id="Color_chosen"]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="Color_chosen"]/div/ul/li[21]').click()  #эксклюзивный
        driver.find_element_by_xpath('//*[@id="Milleage"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="Comment"]').send_keys('Создано svf5 автоматическим тестом при помощи selenium')
        driver.find_element_by_xpath('/html/body/div[1]/advert-editor/main/section/section/div/div/div/div/div[1]/div[37]/div[2]/upload-advert-image/span/a').click() #открываем окно загрузки, далее используем скрипт из AutoIT
        time.sleep(1)
        os.system("C:\\REPO\\eca-front\\src\\app\\auction\\tests\\AutoIT\\upload_foto_1.exe") #загружаем первую фотку
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/advert-editor/main/section/section/div/div/div/div/div[1]/div[37]/div[2]/upload-advert-image/span/a').click()
        time.sleep(1)
        os.system("C:\\REPO\\eca-front\\src\\app\\auction\\tests\\AutoIT\\upload_foto.exe") #загружаем вторую фотку
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/advert-editor/main/section/section/div/div/div/div/div[2]/button').click()
        time.sleep(2)




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
