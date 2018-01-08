import unittest
from selenium import webdriver
import time


class dsf(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_if_else(self):
        driver = self.driver
        driver.get("http://srv-site-dev/account/login")

        login_field = driver.find_element_by_id("Username")
        login_field.send_keys("quotes2@quotes.ru")

        password_filed = driver.find_element_by_id("Password")
        password_filed.send_keys("b0A5QxGa")
        driver.find_element_by_xpath('/html/body/div[2]/main/section/section/form/div[2]/button').click()  # Войти
        time.sleep(2)
        # driver.get("http://super-lk.europlan.ru/auction") - теперь сделали так, что переходить на аукцион не надо, по данному логину сразу на него переадресовывает
        # time.sleep(1)

        current_page_element = driver.find_element_by_xpath('//*[@id="lotList"]/div[2]/ul[1]/li[1]/a')  # берем элемент
        current_page_number = int(current_page_element.text) + 1  # преобразовываем к числу и прибавляем 1
        lots = driver.find_elements_by_class_name('rate-title')  # берём значения элементов определенного класса, в данном случае берем наименования лотов, получается Список(list)
        n = 1 # это для того чтобы видеть сколько раз цикл прошёл

        while True: #lots != 'Nissan X-Trail II FL (Внедорожный 5 дв; 1.997 куб. см - 141 л.с.; АКПП - Полный привод)': # условие, оно правда никогда по идее не сработает,тк в lots просто так не выводится текст
             print(str(n) + ' проход цикла') #печатаем "1 проход цикла", чтобы знать скока раз он отработал
             n+=1 #прибавляем 1, чтобы в след раз вывел 2
             driver.find_element_by_xpath('//*[@id="lotList"]/div[2]/ul[1]/li['+str(current_page_number)+']/a').click() #ищем элемент кнопки пагинации, кликаем на него
             time.sleep(5)
             current_page_number+=1 #добавляем в переменную элемента кнопки пагинации +1
             lots = driver.find_elements_by_class_name('rate-title') # переписываем в лотс наименования лотов, но уже со втророй страницы
             for lot in lots: # чтобы могли сравнить наименования из списка, делаем все через цикл for, "пока есть lot в lots, выводим их" - примерная трактовка
                 if lot.text == 'Nissan X-Trail II FL (Внедорожный 5 дв; 1.997 куб. см - 141 л.с.; АКПП - Полный привод)':  # сравнимаем текст лота с нужным лотом (он на 4 странице), обязательность берем lot.text)
                     driver.find_element_by_xpath('//*[@id="r_905_head"]').click() #если находим кликаем на Характеристики
                     time.sleep(5)
                     print('YYYYYYEEEEEEES') #печатаем yes
                     return # прерываем цикл и выходим из него















    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
