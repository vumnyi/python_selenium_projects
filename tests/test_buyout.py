import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


#открываю вторую страницу аукциона, ищу элемент выкупить за 1 лям, выкупаю, делаю скришот


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_buyout(self):
        driver = self.driver
        driver.get("http://srv-site-dev/account/login")

        login_field = driver.find_element_by_id("Username")
        login_field.send_keys("quotes2@quotes.ru")

        password_filed = driver.find_element_by_id("Password")
        password_filed.send_keys("b0A5QxGa")
        driver.find_element_by_xpath('/html/body/div[2]/main/section/section/form/div[2]/button').click() #Войти
        time.sleep(1)


        driver.get("http://super-lk.europlan.ru/auction")
        title = driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/h1")
        assert title.text == "Автомобили на выкуп"

        time.sleep(2)
        driver.find_element_by_css_selector('#lotList > div.paginator-box.ng-star-inserted > ul:nth-child(1) > li:nth-child(2) > a').click()  # кликаю на 2 страницу
        time.sleep(3)
        # кликаем выкупить за 1000000
        driver.find_element_by_xpath('//*[@id="lotList"]/section[2]/article/div[4]/div[2]/a').click()
        driver.find_element_by_xpath('//*[@id="lotList"]/section[2]/article[1]/div[4]/div/div/button[1]').click()
        driver.get_screenshot_as_file("C:\Python36\screenshots\_buyout.png") #делаем скриншот

  
    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


