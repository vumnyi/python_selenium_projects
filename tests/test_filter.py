import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait




class Login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

  def test_move(self):
    driver = self.driver
    driver.get("http://srv-dockerhost-dev:3089/cars/")
    driver.find_element_by_xpath('//*[@id="details_3"]/div[1]/div[2]/div[1]/div[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="details_3"]/div[1]/div[2]/div[1]/div[1]/input').send_keys('900000') #от 900 000
    driver.find_element_by_xpath('//*[@id="details_3"]/div[1]/div[2]/div[1]/div[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="details_3"]/div[1]/div[2]/div[1]/div[2]/input').send_keys('2500000') #до 2 500 000
    driver.find_element_by_xpath('//*[@id="details_3"]/div[3]/div/div[1]').click() #кликаем Все параметры
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[1]/p-dropdown/div/label').click() # тип кпп
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[1]/p-dropdown/div/div[4]/div/ul/li[2]').click() #мкпп
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[2]/p-dropdown/div/label').click() #привод
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[2]/p-dropdown/div/div[4]/div/ul/li[4]').click() #полный
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[3]/p-dropdown/div/label').click() #двигатель
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[3]/p-dropdown/div/div[4]/div/ul/li[3]').click() #дизель
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[4]/div/div[1]/p-dropdown/div/label').click() #объем от
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[4]/div/div[1]/p-dropdown/div/div[4]/div/ul/li[11]').click() #от 2 л
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[4]/div/div[2]/p-dropdown/div/label').click() #объем до
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[4]/div/div[2]/p-dropdown/div/div[4]/div/ul/li[21]/span').click() # до 5
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[5]/p-dropdown/div/label').click() #мощность
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[1]/div[5]/p-dropdown/div/div[4]/div/ul/li[6]/span').click() #150-175
    driver.find_element_by_xpath('//*[@id="details_2"]/div/div[2]/a[6]').click() #пикап
    driver.find_element_by_xpath('//*[@id="details_3"]/div[3]/div/div[2]/button').click() #найти
    time.sleep(5)
    assert 'Mitsubishi' in driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-search/section/div/div[3]/article/h2').text #сверяем мицубу с текстом из элемента
    assert 'Fiat' in driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-search/section/div/div[4]/article/h2').text #сверяем фиат с текстом из элемента
    assert 'Isuzu' in driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-search/section/div/div[5]/article/h2').text #сверяем исузу с текстом из элемента
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-search/section/div/div[4]/article/ul/li/a/figure').click() #кликаем на модель фиата
    time.sleep(5)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-modifications/section[2]/div/div[6]/div[3]/div[2]/a/p[1]')) #прокручиваемся к элементу
    #можно сделать с переменной
    # element = (driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-modifications/section[2]/div/div[6]/div[1]/div[3]/button')) #появляющийся при наведении элемент
    # action_chains.move_to_element(element).perform() # наводим мышку
    # element.click()
    # а можно всё в одной строке сделать, см ниже
    action_chains.move_to_element(driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-modifications/section[2]/div/div[6]/div[3]/div[3]/button')).click().perform() #наводим на появляющуюся кнопку "купить", кликаем
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[1]/input').send_keys("Трифонов Тест Экзекутович") #заполняем имя
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input').send_keys("9260990099") #заполняем номер
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[3]/input').send_keys("pochta@rf.com") #заполняем почту
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[4]/textarea').send_keys("Трифонов Тест Экзекутович 9260990099 pochta@rf.com") #заполняем коммент
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="request_button"]').click() #нажимаем кнопку Получить расчет
    time.sleep(2)
    print(driver.find_element_by_xpath('//*[@id="request_large"]/div/div/h1').text) #находим и печатаем номер заявки




  def tear_down(self):
    self.driver.quit()


if __name__ == "__main__":
  unittest.main()

