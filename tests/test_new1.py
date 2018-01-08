import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_first(self):
        driver = self.driver
        driver.get("http://srv-site-dev/account/login")

        login_field = driver.find_element_by_id("Username")
        login_field.send_keys("quotes2@quotes.ru")

        password_filed = driver.find_element_by_id("Password")
        password_filed.send_keys("b0A5QxGa")
        driver.find_element_by_xpath('/html/body/div[2]/main/section/section/form/div[2]/button').click() #Войти
        time.sleep(2)


        # марка - ввожу ауди, модель а6,город москва, год 2016, статус активен - показать, проверяю заголовок AAudi A6 IV (Седан; 1.984 куб. см - 180 л.с.; АКПП),
        #  выкупаю, подтверждаю, проверяю заголовок Лот №817 снят с продажи.Победила ставка 1000000 рублей.
        #переходим на аукцирон, проверяем заголовок, кликаем на фильтр, вводим номер лота
        #driver.get("http://super-lk.europlan.ru/auction") - сделали так, что сразу перекидывает
        title = driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/h1")
        assert title.text == "Автомобили на выкуп"
        assert "Список лотов" in driver.title
        #марка
        driver.find_element_by_css_selector("#f_1_head").click() #фильтр

        driver.find_element_by_css_selector("#f_1 > div > div.item.item1 > p-dropdown > div > label").click() #дропдаун/марка
        driver.implicitly_wait(3)  #time.sleep(1)
        driver.find_element_by_xpath('//*[@id="f_1"]/div/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[3]').click() #ауди
        time.sleep(1)
        #модель
        driver.find_element_by_css_selector("#f_1 > div > div.item.item2 > p-dropdown > div > label").click() #дропдаун/модель
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="f_1"]/div/div[2]/p-dropdown/div/div[4]/div[2]/ul/li[4]').click() #а6
        time.sleep(1)
        #город
        # driver.find_element_by_css_selector('#f_1 > div > div.item.item3 > p-multiselect > div > div.ui-multiselect-label-container > label').click() #дропдаун/город
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="f_1"]/div/div[3]/p-multiselect/div/div[4]/div[2]/ul/li[1]').click() #москва
        # time.sleep(1)
        #год выпуска
        driver.find_element_by_css_selector("#f_1 > div > div:nth-child(4) > p-dropdown > div > label").click() #дропдаун/годы выпуска
        driver.implicitly_wait(3)  #time.sleep(1)
        driver.find_element_by_xpath('//*[@id="f_1"]/div/div[4]/p-dropdown/div/div[4]/div[2]/ul/li[16]').click() #2016
        driver.implicitly_wait(3)  #time.sleep(1)
        #статус
        driver.find_element_by_css_selector("#f_1 > div > div:nth-child(5) > p-dropdown > div > label").click() #дропдаун/статусы
        driver.implicitly_wait(3)  #time.sleep(1)
        driver.find_element_by_xpath('//*[@id="f_1"]/div/div[5]/p-dropdown/div/div[4]/div/ul/li[2]').click() #активен
        driver.implicitly_wait(5)  #time.sleep(1)
        #кнопка показать
        driver.find_element_by_xpath('//*[@id="f_1"]/div/div[7]/button').click()
        time.sleep(3)
        # проверяем название лота
        caption = driver.find_element_by_xpath('//*[@id="lotList"]/section[2]/article/div[3]/div/div[1]').text
        assert caption == 'Audi A6 IV седан 4 дв, 2.0 бензин (179.52 л.с.)'
        # кликаем выкупить за 1000000, выбираем "нет", чтобы подтвердить выкуп за лям, поставить 1 в button
        #driver.find_element_by_xpath('//*[@id="lotList"]/section[2]/article/div[4]/div[2]/a').click()
        #river.find_element_by_xpath('//*[@id="lotList"]/section[2]/article[1]/div[4]/div/div/button[2]').click()
        driver.implicitly_wait(3)  #time.sleep(3)

        #чтобы нужные лоты снова активировать надо запустить скрипт DB
        #вводим номер лота
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[1]/div/div/div[6]/input").send_keys("896")
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[1]/div/div/div[7]/button").send_keys(Keys.ENTER)
        time.sleep(2)
        #проверяем что нашли тот лот, который нам нужен
        lot = driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article/div[3]/div/div[1]")
        assert lot.text == "Lada Priora I FL хетчбэк 5 дв, 1.6 бензин (98 л.с.)"
        #print(lot.text)
        #текущая ставка + 1000
        title1 = driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article/div[4]/div[1]/div[1]/div/span").text #получаем текст элемента
        a = ''.join(str.split(title1)) #убираем пробел
        aga = int(a[0:7]) + 1000 #берем строку из а (на данный момент 2 571 000, поэто 0:7) и преобразовываем в число, после чего прибавляем 1000
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article/div[4]/div[1]/div[2]/input").send_keys(aga) #вводим новую ставку
        driver.get_screenshot_as_file("C:\Python36\screenshots\screen.png") #делаем скриншот
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article/div[4]/div[1]/div[2]/button").click()
        driver.implicitly_wait(3)  #time.sleep(1)
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article[1]/div[4]/div[2]/textarea").send_keys("Комментарий ТЕСТ123")
        driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article/div[4]/div[1]/div/button[1]").click() #подтверждаем
        #берем текст из текущей ставки и сравниваем со ставкой которую сделали
        aga_1 = driver.find_element_by_xpath("/html/body/app/auction/div[2]/auction-list/main/div/div[1]/section[2]/article[1]/div[4]/div[1]/div[1]/div[1]/span").text
        b = ''.join(str.split(aga_1)) #убираем пробел
        aga_2 = int(b[0:7]) #берем нужные нам символы
        assert aga == aga_2


    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


