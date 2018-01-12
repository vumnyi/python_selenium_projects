import unittest
from selenium import webdriver
import time
import pyodbc
from selenium.webdriver import ActionChains




class Login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

  def test_trailer(self):
    driver = self.driver
    driver.get("http://srv-dockerhost-dev:3089/cars")

    babka = ('Прицепы Полуприцепы', '9096660066', 'trailer@sxds.ru', 'комментарий трейлер 123456798 - 000 ваомпвлопдло hjdsjhfjhs')  # здесь прлосто список, чтобы вставлять значения в функцию xpath_send_k

    def xpath_click(xp_click): #клик по xpath
      '''Find XPATH and CLICK element'''
      driver.find_element_by_xpath(xp_click).click()


    def xpath_send_k(xp_send_k, babka):  # функция принимает два параметра xpath и значение из babka
      '''Find XPATH and SEND KEYS element'''
      driver.find_element_by_xpath(xp_send_k).send_keys(babka)

    xpath_click('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[4]')

    # xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/label')
    # brands = driver.find_elements_by_xpath('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/div[4]/div[2]/ul/li')
    # li = 2
    # for i in brands:
    #   xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/div[4]/div[2]/ul/li[' + str(li) + ']')
    #   xpath_click('//*[@id="filterBody"]/div[1]/div[2]/p-dropdown/div/label')
    #   li += 1
    #   if li == 170:
    #     break

    #
    xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
    views = driver.find_elements_by_xpath('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li')
    li = 2
    for i in views:
         xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/div[4]/div[2]/ul/li[' + str(li) + ']')
         xpath_click('//*[@id="filterBody"]/div[1]/div[1]/p-dropdown/div/label')
         li += 1
         if li == 61:
            break
    time.sleep(2)

    xpath_click('//*[@id="filterBody"]/div[3]/button')
    time.sleep(2)
    xpath_click('/html/body/app/auto/div[2]/main/auto-search/section/div/div[3]/article/ul/li/a/div/p')
    #
    actions = ActionChains(driver)
    element = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-modifications/section[2]/div/div[5]/div/div[3]/button')
    actions.move_to_element(element).perform()
    element.click()
    time.sleep(2)
    # xpath_click('//*[@id="request_large"]/form/ul/li[1]/input')
    xpath_send_k('//*[@id="request_large"]/form/ul/li[1]/input', babka[0])
    time.sleep(2)
    xpath_send_k('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input', babka[1])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[3]/input', babka[2])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[4]/textarea', babka[3])
    xpath_click('//*[@id="request_button"]')
    time.sleep(5)
    number_request = driver.find_element_by_xpath('//*[@id="request_large"]/div/div/h1').text
    print(number_request[20:])  # берем номер заявки без пробела
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv')  # Создаем соединение с нашей базой данных
    cursor = cnxn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor.execute("select top 1 [RequestNumber] from [Site-Dev].[dbo].[Requests] ORDER BY id DESC") # используем в запросе свою переменную,таким образом {0} - здесь обозначение переменной, .format(number_request) - объясняем где взять переменную
    result = cursor.fetchall() # Получаем результат сделанного запроса
    print(result[0][0]) # берем в списке 0 элемент (это тоже список) и уже в нём берем 0 элемент
    assert number_request[20:] == result[0][0] #ВНИМАТЕЛЬНО берем из переменных только необходимые ЗНАЧЕНИЯ
    cnxn.close() # Не забываем закрыть соединение с базой данных

    driver.back()
    driver.get('chrome://settings/clearBrowserData') #https://intoli.com/blog/clear-the-chrome-browser-cache/ как удалить куки
    time.sleep(2)
    driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataDialog')
    driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm').click()
    time.sleep(5)
    driver.back()


    xpath_send_k('//*[@id="request_large"]/form/ul/li[1]/input', babka[0])
    time.sleep(2)
    xpath_send_k('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input', babka[1])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[3]/input', babka[2])
    xpath_send_k('//*[@id="request_large"]/form/ul/li[4]/textarea', babka[3])
    xpath_click('//*[@id="request_button"]')
    time.sleep(5)
    number_request = driver.find_element_by_xpath('//*[@id="request_large"]/div/div/h1').text
    print(number_request[20:])  # берем номер заявки без пробела
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv')  # Создаем соединение с нашей базой данных
    cursor = cnxn.cursor()  # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor.execute("select top 1 [RequestNumber] from [Site-Dev].[dbo].[Requests] ORDER BY id DESC")  # используем в запросе свою переменную,таким образом {0} - здесь обозначение переменной, .format(number_request) - объясняем где взять переменную
    result = cursor.fetchall()  # Получаем результат сделанного запроса
    print(result[0][0])  # берем в списке 0 элемент (это тоже список) и уже в нём берем 0 элемент
    assert number_request[20:] == result[0][0]  # ВНИМАТЕЛЬНО берем из переменных только необходимые ЗНАЧЕНИЯ
    cnxn.close()  # Не забываем закрыть соединение с базой данных




  def tear_down(self):
    self.driver.quit()

  if __name__ == "__main__":
    unittest.main()

