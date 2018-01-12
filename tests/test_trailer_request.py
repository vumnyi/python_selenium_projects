import unittest
from selenium import webdriver
import time
import pyodbc



class Login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

  def test_trailer(self):
    driver = self.driver
    driver.get("http://srv-dockerhost-dev:3089/cars")

    babka = ('Прицепы Полуприцепы', '0909567899', 'trailer@sxds.ru', 'комментарий трейлер 123456798 - 000 ваомпвлопдло hjdsjhfjhs')  # здесь прлосто список, чтобы вставлять значения в функцию xpath_send_k

    def xpath_click(xp_click): #клик по xpath
      '''Find XPATH and CLICK element'''
      driver.find_element_by_xpath(xp_click).click()


    def xpath_send_k(xp_send_k, babka):  # функция принимает два параметра xpath и значение из babka
      '''Find XPATH and SEND KEYS element'''
      driver.find_element_by_xpath(xp_send_k).send_keys(babka)

    xpath_click('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[3]') #прицепы/полуприцепы
            #кликаем по всем видам
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label') #кликаем по Вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[2]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[3]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[4]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[5]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[6]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[7]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[8]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[9]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[10]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[11]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[12]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[13]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[14]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[15]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[16]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[17]')
    #кликаем по грузоподъемности, поочередно выбираем все
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[2]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[3]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[4]')

    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[5]')

    xpath_click('//*[@id="filterBody"]/div[2]/a') #сбросить
    time.sleep(1)

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[3]') #полуприцеп бортовой

    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label') #грузопод
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[5]') #от 24 тонн
    xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/label') #marka
    xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/div[4]/div[2]/ul/li[4]') #maz
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[1]/div[3]/p-dropdown/div/label') #model
    xpath_click('//*[@id="filterBody"]/div[1]/div[3]/p-dropdown/div/div[4]/div[2]/ul/li[2]') #9386
    xpath_click('//*[@id="filterBody"]/div[2]/button')
    time.sleep(3)
    assert driver.find_element_by_xpath('//*[@id="m_title"]').text == '9386'
    xpath_click('/html/body/app/auto/div[2]/main/auto-modifications/section[1]/div/div/figcaption/button') # кликаем Рассчитать лизинг
    assert driver.find_element_by_xpath('//*[@id="request_large"]/form/h2').text == 'Оформите заявку'
    xpath_send_k('//*[@id="request_large"]/form/ul/li[1]/input', babka[0])
    time.sleep(2)
    xpath_send_k('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input', babka[1])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[3]/input', babka[2])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[4]/textarea', babka[3])
    xpath_click('//*[@id="request_button"]')
    time.sleep(4)

    number_request = driver.find_element_by_xpath('//*[@id="request_large"]/div/div/h1').text
    print(number_request[20:])  # берем номер заявки без пробела

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv')  # Создаем соединение с нашей базой данных
    cursor = cnxn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    # cursor.execute("select * from [Site-Dev].[dbo].[Requests] where [RequestNumber] = '{0}'".format(number_request)) # используем в запросе свою переменную,таким образом {0} - здесь обозначение переменной, .format(number_request) - объясняем где взять переменную
    cursor.execute("select top 1 [RequestNumber] from [Site-Dev].[dbo].[Requests] ORDER BY id DESC") # используем в запросе свою переменную,таким образом {0} - здесь обозначение переменной, .format(number_request) - объясняем где взять переменную
    result = cursor.fetchall() # Получаем результат сделанного запроса
    print(result[0][0]) # берем в списке 0 элемент (это тоже список) и уже в нём берем 0 элемент

    assert number_request[20:] == result[0][0] #ВНИМАТЕЛЬНО берем из переменных только необходимые ЗНАЧЕНИЯ

    cnxn.close() # Не забываем закрыть соединение с базой данных




  def tear_down(self):
      self.driver.quit()

  if __name__ == "__main__":
    unittest.main()



