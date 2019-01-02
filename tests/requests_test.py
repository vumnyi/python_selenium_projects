import requests
import json
from requests_toolbelt import MultipartEncoder #http://toolbelt.readthedocs.io/en/latest/user.html
from requests_ntlm import HttpNtlmAuth

def status_code():#функция печатающая текст в зависимости от вернувшегося кода
  if r.status_code == 200:
    print('Status code - 200')
    print(r.text)
  else:
    print('Status code not 200')
    print(r.status_code)
    print(r.reason)

#получение данных при заходе на http://srv-site-dev/
url = 'http://srv-site-dev/api/search/post'
data = {}
headers = {}
data = {"carTypeId": "1"}
headers = {"accept": "application/json, text/plain, */*", "accept-encoding": "gzip, deflate",
           "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "connection": "keep-alive",
           "content-type": "application/json;charset=UTF-8", "host": "srv-site-dev", "origin": "srv-site-dev", "referer": "srv-site-dev",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}

r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()
#
# # #Запрос без параметров на создание заявки автомаркет http://srv-dockerhost-dev:3089/commercial/search
url = 'http://srv-site-dev/api/application/leasingshort'
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()

#
# # # #Запрос с параметрами
url = 'http://srv-site-dev/api/application/leasingshort'
headers = {'referer': 'http://srv-dockerhost-dev:3089/cars'}
data = {'acceptTerms': 'true', 'applicationKind': 'LeasingShortRegular', 'commentary': 'комментарий тест test', 'email': 'test@test.ru',
         'firstName': 'Имя', 'phone': '9094545645' }
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()
# # #
# #Запрос на автомаркете get-hash/
url = 'http://srv-site-dev/api/auto/get-hash'
data = {}
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()
# #
# Запрос на автомаркете при выборе марки БМВ, возвращает модель
url = 'http://srv-site-dev/api/vehicle-taxonomy/supertypebrands/1846/models?superTypeId=8&&official=true'
r = requests.get(url, json=data, headers=headers, timeout=(30, 30))
status_code()
# #
# # #Запрос на автомаркете get-hash, в котором указываются все параметры выбранные в фильтр, ищем Киа
url = 'http://srv-site-dev/api/auto/get-hash/'
data = {'bodyType': '12', 'brand': '8014', 'drive': '2', 'engineDisplacementMax': '1.6', 'engineDisplacementMin': '0.2', 'engineType': '1',
'gearbox': '2', 'model': '138849', 'power': '70-100', 'price': [597000, 3864000], 'vehicleSuperTypes': [8]}
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()

# #Запрос на автомаркете get-hash, в котором указываются все параметры выбранные в фильтр,но можем указать все значения вручную через input
url = 'http://srv-site-dev/api/auto/get-hash/'
data = {'bodyType': input('Введите bodyType: '), 'brand': input('Введите brand: '),  'drive': input('Введите drive: ')}
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
# status_code()

# #Загрузка изображений в адвёрты
url = 'http://srv-site-dev/api/auto/upload-advert-images'
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()

# #Загрузка изображений в лоты
url = 'http://srv-site-dev/api/auto/upload-lot-images'
r = requests.post(url, json=data, headers=headers, timeout=(30, 30))
status_code()

#запрос ТипаТС при создании лота/адвёрта
url = 'http://srv-dockerhost-dev:3093/api/vehicletaxonomy/brands?supertypeId=6' #- вместо 6, через цикл прогоняем все supertypeid и отправляем запрос с ними
for i in range(6, 15):
  url = 'http://srv-dockerhost-dev:3093/api/vehicletaxonomy/brands?supertypeId='+ str(i) +''
  r = requests.get(url, json=data, headers=headers, timeout=(30, 30))
  status_code()
#

#получаем виндовый access_token
#чтобы узнать на какой урл отправлять запрос, заходим на страницу где отправляется запрос,
#предварительно очистив Apllication-Clear storage в консоли
#обновляем страницу http://srv-dockerhost-dev:3093/adverts/advert и смотрим Request URL:https://auth-dev.europlan.ru/Account/windows/token?clientId=epSite&resource=quotesApi&scope=openid%20profile%20quotesApi%20offline_access
url = "https://auth-dev.europlan.ru/account/windows/token?clientId=epSite&scope=openid%20profile%20quotesApi%20offline_access" #посдтавляем его
r = requests.get(url, auth=HttpNtlmAuth('MSC\\svf5', 'qweBNM123')) #отправляем виндовые домен,логин/пароль
a = json.loads(r.text) #преобразовывае всё в jsonчик
c = a['access_token'] #и берем значение access_token

#это проверка что по токену меня определяет
#и оборачиваем это в try except чтобы можно было использваоть токен, пока он не перестал был валидным по таймауту
token = 'Bearer ' + c #здесь конкатенируем строки
url = 'http://srv-dockerhost-dev:3093/api/auth/user'
headers = {'Authorization': token}
data = {}
try:
  r = requests.get(url, json=data, headers=headers, timeout=(30, 30)) #пробуем отправить запрос с токеном
except requests.exceptions.ReadTimeout:
  print('Таймаут на чтение')
except requests.exceptions.ConnectTimeout:
  print('Таймаут на соединение')

if r.status_code == 200:
  print("Токен рабочий")
else: #если не рабочий получаем заново
  print(r.status_code)
  url = "https://auth-dev.europlan.ru/account/windows/token?clientId=epSite&scope=openid%20profile%20quotesApi%20offline_access"  # подставляем его
  r = requests.get(url, auth=HttpNtlmAuth('MSC\\svf5', 'qweBNM123'))  # отправляем виндовые домен,логин/пароль
  a = json.loads(r.text)  # преобразовывае всё в jsonчик
  c = a['access_token']  # и берем значение access_token
  token = 'Bearer ' + c



#Запрос на добавление новой модификации
url = 'http://srv-dockerhost-dev:3093/api/vehicletaxonomy/request-new-modification'

'''в каком формате передается запрос - Content-Type:multipart/form-data; boundary=----WebKitFormBoundarySAUBQQDMaiDtWQVB
чтобы передать параметры такого вида:
Request Payload

------WebKitFormBoundarySAUBQQDMaiDtWQVB
Content-Disposition: form-data; name="files"; filename="9782184s-960.jpg"
Content-Type: image/jpeg

------WebKitFormBoundarySAUBQQDMaiDtWQVB
Content-Disposition: form-data; name="year"

В data пишем данные, которые берем из Response консоли
'''
# data = MultipartEncoder(fields=
#         {"brand": "sdf",
#          "model": "sdf",
#          "year":"sdf",
#          "bodyType":"dsf",
#          "wheelBase":"sdf",
#          "doorsCount":"sdf",
#          "engineType":"sdf",
#          "enginePower":"sdf",
#          "gearbox":"dsf",
#          "drive":"sdf",
#          "link":"sJKHKdf",
#          "manager":"Фунтиков Сергей Владимирович"})

data = MultipartEncoder ({"brand": 'dfg'}) #так тоже работает, без fields
headers = {
  'Authorization': token, #сюда подставялем токен
  'Content-Type': data.content_type #сюда пишем формат в котором передаём
}
r = requests.post(url, data=data, headers=headers)
status_code()
print()

#загрузка фото адвёртов в админке
data = MultipartEncoder(fields={"images": ('cq5.jpg', '')})
headers = {
  'Authorization': token,  # сюда подставялем токен
  'Content-Type': data.content_type  # сюда пишем формат в котором передаём
          }
url = 'http://srv-site-dev/api/auto/upload-advert-images' #урл куда отправляем
r = requests.post(url, data=data, headers=headers) #параметры
print('Загрузка фото в адвертах')
try:
  assert 200 == r.status_code #проверяем что код ответа 200
  print("Успех")
except:
  status_code()
print() #пустая строка


#загрузка фото лотов в админке

data = MultipartEncoder(fields={'images': ('Audi-A6-Avant-3.0-TDI-quattro-Innenraum.jpg', '')}) #https://pypi.python.org/pypi/requests-toolbelt, отправляем параметры фото в таком виде, по ссылке можно почитать

headers = {
  'Authorization': token,  # сюда подставялем токен
  'Content-Type': data.content_type,  # сюда пишем формат в котором передаём
          }
url = 'http://srv-site-dev/storagedfile/upload-images' #урл куда отправляем
r = requests.post(url, data=data, headers=headers) #параметры
print('Загрузка фото в лотах')
try:
  assert 200 == r.status_code #проверяем что код ответа 200
  print("Успех")
except:
  status_code()
print() #пустая строка





