import unittest
from selenium import webdriver
import time



class Login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

  def test_begin(self):
    driver = self.driver
    driver.get("http://srv-dockerhost-dev:3089/cars")


    def xpath_click(xp_click):
      '''Find XPATH and CLICK element'''
      driver.find_element_by_xpath(xp_click).click()


    #babka = {'name': 'Имечко', 'telef': '9096660066', 'email': 'ssd@sxds.ru', 'comment': 'всаипвап ьовдлл ДОЛРЛОврьылоамирло ыылорлор345sdfsdff'} #здесь делал словарь ключ: значение
    babka = ('Имечко Отчеcтво Фамилия', '9096660066', 'ssd@sxds.ru', 'комментарий тест 123456798 - 000 ваомпвлопдло hjdsjhfjhs') #здесь прлосто список, чтобы вставлять значения в функцию xpath_send_k


    def xpath_send_k(xp_send_k, babka): #функция принимает два параметра xpath и значение из babka
      '''Find XPATH and SEND KEYS element'''
      driver.find_element_by_xpath(xp_send_k).send_keys(babka)

    xpath_click('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[2]') #коммерч
    time.sleep(2)
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label') #вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[2]/span') #вахтовый
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Пассажирских мест'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[3]')  # городской
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Пассажирских мест'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[4]')  # грузов борт
    time.sleep(1)
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[5]')  # грузовой рефри
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[6]')  # грузовой самос
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[7]')  # грузо пассаж фург
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[8]')  # изотер фур
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[9]')  # пикап
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[10]')  # промтовар
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[11]')  # седельный
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[13]')  # хлеб фур
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Макс. масса'

    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')  # вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[12]')  # тур автоб
    time.sleep(1)
    assert driver.find_element_by_xpath('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label').text == 'Пассажирских мест'




    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label') #вид
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[14]') #цельнометалл
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/label') #марка
    xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/div[4]/div[2]/ul/li[5]') #лада
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[1]/div[3]/p-dropdown/div/label') #модель
    xpath_click('//*[@id="filterBody"]/div[1]/div[3]/p-dropdown/div/div[4]/div[2]/ul/li[3]') #ларгус
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/label') #типкпп
    xpath_click('//*[@id="filterBody"]/div[1]/div[4]/p-dropdown/div/div[4]/div/ul/li[2]') #мкпп
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/label') #макс масса
    xpath_click('//*[@id="filterBody"]/div[1]/div[5]/p-dropdown/div/div[4]/div/ul/li[3]/span') #1,5 - 3 т
    time.sleep(1)
    xpath_click('//*[@id="filterBody"]/div[2]/a') #сбросить


    xpath_click('//*[@id="request_large"]/form/ul/li[1]/input') #кликаем на имя
    # xpath_send_k('//*[@id="request_large"]/form/ul/li[1]/input', babka['name']) #вводится текст из переменной, здесь использовал значения из словаря с ключ-значения, но это оказалось неудобно, каждый раз вводить ключ, поэтому сейчас беру просто по индексу
    xpath_send_k('//*[@id="request_large"]/form/ul/li[1]/input', babka[0]) # передаем два аргумента, xpath и значение babka вводится текст из переменной babka по индексу 0
    #text = '9090000000' #меняем значение переменной
    time.sleep(2)
    xpath_click('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input')  #кликаем на телефон
    # xpath_send_k('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input', babka['telef']) #вводим номер
    xpath_send_k('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input', babka[1]) #вводим номер
    #text = 'sdfdsfqwe483583@sadfdsf.ru' #меняем переменную на емейл
    xpath_click('//*[@id="request_large"]/form/ul/li[3]/input') #кликаем на ваш емейл
    # xpath_send_k('//*[@id="request_large"]/form/ul/li[3]/input', babka['email']) #вводим почту
    xpath_send_k('//*[@id="request_large"]/form/ul/li[3]/input', babka[2]) #вводим почту
    #text = 'Comment Комментарий ТЕСТ 1234567980000' #меняем переменную
    xpath_click('//*[@id="request_large"]/form/ul/li[4]/textarea') #кликаие на коммент
    # xpath_send_k('//*[@id="request_large"]/form/ul/li[4]/textarea', babka['comment']) #вводим коммент
    xpath_send_k('//*[@id="request_large"]/form/ul/li[4]/textarea', babka[3]) #вводим коммент
    time.sleep(2)
    xpath_click('//*[@id="request_button"]') #нажимаем отправить
    time.sleep(5)















  def tear_down(self):
      self.driver.quit()

  if __name__ == "__main__":
    unittest.main()

