from selenium_fixture import *
from application import *


def test_page_sort(app):
  app.go_to_shop('https://shop.by/')  # передеаем нужный урл и заходим на страницу
  app.go_to_section('Компьютеры', 'Ноутбуки')  # передаем нужные нам разделы
  app.choice_brand('Dell', 'Lenovo', 'HP')  # передаем интересующие нас марки
  app.choice_price(700, 1500)  # передаем сумму
  app.choice_display_size(12, 12.1, 12.5, 13, 13.1, 13.3, 13.4, 13.5)  # передаем нужные размеры дисплея
  app.button_show()  # нажимаем Показать
  app.count()  # сохраняем и печатаем количество элементов
  app.sort('max')  # сортируем по цене (сначала дорогие)
  first_name = app.parse_first_name()  # название первой модели
  app.sort('min')  # сортируем по цене (сначала дешевые и переходим на последнюю страницу)
  last_name = app.parse_last_name()  # название последней модели
  assert first_name == last_name


