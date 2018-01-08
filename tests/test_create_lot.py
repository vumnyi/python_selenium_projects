import unittest
from selenium import webdriver
import time



class all_in(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_create_lot(self):
        driver = self.driver
        driver.get("http://srv-site-dev/account/login")
        driver.find_element_by_xpath('//*[@id="Username"]').send_keys('7252395')
        driver.find_element_by_xpath('//*[@id="Password"]').send_keys('22061941')
        driver.find_element_by_xpath('/html/body/div[2]/main/section/section/form/div[2]/button').click()

        driver.find_element_by_xpath('/html/body/div[2]/div[4]/a[4]').click() # список лотов
        driver.find_element_by_xpath('/html/body/div[1]/auction-list-admin/main/section/section/a').click() #добавить лот
        driver.find_element_by_xpath('//*[@id="VehicleType_chosen"]/a').click() #тип авто
        driver.find_element_by_xpath('//*[@id="VehicleType_chosen"]/div/ul/li[3]').click() #легковой
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Brand_chosen"]/a').click() #марка
        driver.find_element_by_xpath('//*[@id="Brand_chosen"]/div/ul/li[32]').click() #lamborghini
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Model_chosen"]/a').click() #модель
        driver.find_element_by_xpath('//*[@id="Model_chosen"]/div/ul/li[2]').click() #huracan
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Modification_chosen"]/a').click()  # модификация
        driver.find_element_by_xpath('//*[@id="Modification_chosen"]/div/ul/li[1]').click()  #купе
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="Generation_chosen"]/a').click()  # поколение
        driver.find_element_by_xpath('//*[@id="Generation_chosen"]/div/ul/li[20]').click()  #хх
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Restyling_chosen"]/a').click()  # рестайлинг
        driver.find_element_by_xpath('//*[@id="Restyling_chosen"]/div/ul/li[6]').click()  # 5
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # скролл

        driver.find_element_by_xpath('//*[@id="Year_chosen"]/a').click()  # год выпуска
        driver.find_element_by_xpath('//*[@id="Year_chosen"]/div/ul/li[1]').click()  # 2017
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Milleage"]').send_keys('66 666')  # пробег 66 666
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="Color_chosen"]/a').click()  # цвет
        driver.find_element_by_xpath('//*[@id="Color_chosen"]/div/ul/li[21]').click()  # эксклюзивный
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="City_chosen"]/a').click()  # город
        driver.find_element_by_xpath('//*[@id="City_chosen"]/div/ul/li[2]').click()  # санкт-петербург
        driver.find_element_by_xpath('//*[@id="OwnerCount"]').send_keys('13')  # кол-во владельцев 13
        driver.find_element_by_xpath('//*[@id="SuzId"]').send_keys('132456789')  # заявка в суз 123456789
        driver.find_element_by_xpath('//*[@id="Vin"]').send_keys('98765432103454354')  # вин 98765432103454354
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="Manager_chosen"]/a').click()  # менеджер
        driver.find_element_by_xpath('//*[@id="Manager_chosen"]/div/ul/li[10]').click()  # приймак
        driver.find_element_by_xpath('//*[@id="Comment"]').send_keys('Создано svf5 автоматическим тестом при помощи selenium')  # комментарий "создано автоматически..."

        #добавляем фото, по xpath кнопки загрузить фото, элемент должен быть input
        driver.find_element_by_xpath("/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[1]/div[24]/div[2]/upload-storaged-file/span/input").send_keys('C:\\Users\\svf5\\Desktop\\материал по задачам\\тачки\\48d17625e8f2a612-main.jpg')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[1]/div[24]/div[2]/upload-storaged-file/span/input").send_keys('C:\\Users\\svf5\\Desktop\\материал по задачам\\тачки\\huracan-coupe.jpg')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[1]/div[24]/div[2]/upload-storaged-file/span/input").send_keys('C:\\Users\\svf5\\Desktop\\материал по задачам\\тачки\\Lamborghini-Huracan-LP580-2-2016-2017-salon-min.jpg')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[1]/div[24]/div[2]/upload-storaged-file/span/input").send_keys('C:\\Users\\svf5\\Desktop\\материал по задачам\\тачки\\39f58c-18920132_1236997796409231_478692431878965951_n.jpg')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[1]/div[24]/div[2]/upload-storaged-file/span/input").send_keys('C:\\Users\\svf5\\Desktop\\материал по задачам\\тачки\\Huracan_1.jpg')

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="Duration"]').send_keys('400')  # длительность 400
        driver.find_element_by_xpath('//*[@id="IsActive"]').click()  # активен
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/auction-editor/main/section/section/div/div/div/div/div[2]/button').click()
        time.sleep(5)









    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
