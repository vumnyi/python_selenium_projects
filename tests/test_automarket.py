import unittest
from selenium import webdriver
import time
import pyodbc




class Login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

  def test_assert_send_request_check_in_DB(self):
    driver = self.driver
    driver.get("http://srv-dockerhost-dev:3089/cars")
    #self.assertIn('Автомаркет', driver.title) #проверяем наименвоание страницы
    assert 'Автомаркет' in driver.title #проверяем наименование страницы
    h1 = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[1]') #заголовок
    assert h1.text == 'Новые автомобили'
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/header/section/div/div/div[1]/div/img').is_displayed() #лого
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/header/section/div/div/div[2]/a').is_displayed() #телефон1
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/header/section/div/div/div[3]/a').is_displayed() #телефон2
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/header/div/a').is_displayed() #Автомаркет
    cars = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[1]') #в фильтре Легковые
    assert cars.text == 'Легковые'
    commercial = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[2]') #в фильтре Коммерческие
    assert commercial.text == 'Коммерческий'
    trailer = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[3]') #в фильтре Прицепы/полуприцепы
    assert trailer.text == 'Прицепы/полуприцепы'
    special = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-filter/section/div[2]/section/section/div[2]/section[1]/div[4]') #в фильтре Спецтехника
    assert special.text == 'Спецтехника'
    button = driver.find_element_by_xpath('//*[@id="details_3"]/div[3]/div/div[2]/button') #в фильтре кнопка Найти
    assert button.text == 'Найти'
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #скроллим страницу
    request = driver.find_element_by_xpath('//*[@id="request_large"]/form/h2') #заголовок Оформите заявку
    assert request.text == 'Оформите заявку'
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[1]').is_displayed() #Ваше имя
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[2]').is_displayed() #Ваше телефон
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[3]').is_displayed() #Ваше емейл
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[4]').is_displayed() #Ваше комментарий
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/footer').is_displayed() #блок футера
    driver.find_element_by_xpath('/html/body/app/auto/div[2]/footer/section/p/a[2]/img').is_displayed() #лого сафмара
    driver.find_element_by_css_selector('form.box > div:nth-child(4) > p:nth-child(1) > label:nth-child(1) > span:nth-child(2)').is_selected()
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[1]/input').send_keys('Тестовое имя')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[2]/p-inputmask/input').send_keys('9091324567')
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[3]/input').send_keys('test@test.ru')
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[4]/textarea').send_keys('Тестовое имя Телефон - 9091324567 Почта - test@test.ru')
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[5]/p-dropdown/div/label').click()
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[5]/p-dropdown/div/div[4]/div[2]/ul/li[28]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[6]/p-dropdown/div/label').click()
    driver.find_element_by_xpath('//*[@id="request_large"]/form/ul/li[6]/p-dropdown/div/div[4]/div[2]/ul/li[3]').click()
    driver.find_element_by_xpath('//*[@id="request_button"]').click()
    time.sleep(2)
    number_request = driver.find_element_by_xpath('/html/body/app/auto/div[2]/main/auto-index/auto-request-large/section/div/div/h1').text #берем тект из заявки Номер вашей заявки: КЛ171227-6925
    time.sleep(5)
    number_request = number_request[19:] #парсим конкретный номер ' КЛ171227-6925'
    number_request = ''.join(str.split(number_request)) #убираем пробелы, тк у нас они есть - ' КЛ171227-6925'
    print(number_request) #смотрим какой номер заявки получился
    # подключаемся к базе
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=db-site-stage;DATABASE=Site-Dev;UID=fo;PWD=flfdfqntifhbrfghjlflbv') # Создаем соединение с нашей базой данных
    cursor = cnxn.cursor() # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    # cursor.execute("update [Site-Dev].[dbo].[Requests] set [Email] = '111@lolka' where [RequestNumber] = '{0}'".format(number_request)) использовал дял проверки, что запрос выполняется
    cursor.execute("select * from [Site-Dev].[dbo].[Requests] where [RequestNumber] = '{0}'".format(number_request)) # используем в запросе свою переменную,таким образом {0} - здесь обозначение переменной, .format(number_request) - объясняем где взять переменную
    result = cursor.fetchall() # Получаем результат сделанного запроса
    print(result)
    # cnxn.commit() # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить
    cnxn.close() # Не забываем закрыть соединение с базой данных
    time.sleep(2)


  def tear_down(self):
    self.driver.quit()


if __name__ == "__main__":
  unittest.main()


