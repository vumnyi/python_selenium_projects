"""Tests for Products page"""
from selenium.webdriver.common.alert import Alert
from page_objects import MainPage, UserPage, ProductPage, CartPage, BasePage, CatalogPage, AdminPage
from page_objects.common.Headings import Headings

PRODUCT_NAME = 'TESLA'
MODEL = 'MODEL S'
NEW_MODEL = 'ROADSTER'


def test_add_item(browser, admin_autorization):
    """Добавляем новый продукт в админке, используем фикстуру
     для авторизации в админке, проверяем что наш продукт в списке"""
    AdminPage(browser).navigation_panel_click('Catalog'). \
        section_item_click('Products')
    assert Headings(browser).get_h1_text() == 'Products'
    AdminPage(browser).add_new_button_click() \
        .product_inputs("Product Name", PRODUCT_NAME) \
        .product_inputs("Meta Tag Title", 'TESLA TEST') \
        .product_topics_click('Data') \
        .product_inputs("Model", MODEL) \
        .product_inputs("Price", '45000') \
        .product_inputs("Quantity", '13') \
        .save_product_button_click() \
        .filter_inputs("Product Name", PRODUCT_NAME) \
        .filter_inputs("Model", MODEL) \
        .filter_button_click()
    try:
        assert PRODUCT_NAME in AdminPage(browser).products_names_in_list()
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + PRODUCT_NAME)


def test_edit_item(browser, admin_autorization):
    """Редактируем продукт в админке (меняем модель), используем фикстуру
     для авторизации в админке, провеярем что новая модель в списке"""
    AdminPage(browser).navigation_panel_click('Catalog') \
        .section_item_click('Products') \
        .filter_inputs("Product Name", PRODUCT_NAME) \
        .filter_button_click().edit_button_click() \
        .product_topics_click('Data') \
        .product_inputs("Model", NEW_MODEL) \
        .save_product_button_click()
    try:
        assert NEW_MODEL in AdminPage(browser).models_names_in_list()
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + NEW_MODEL)


def test_delete_item(browser, admin_autorization):
    """Удаляем продукт в админке, используем фикстуру
    для авторизации в админке, проверяем что новая модель не в списке"""
    AdminPage(browser).navigation_panel_click('Catalog') \
        .section_item_click('Products') \
        .filter_inputs("Product Name", PRODUCT_NAME) \
        .filter_button_click() \
        .product_list_checkbox_click(NEW_MODEL) \
        .delete_button_click()
    Alert(browser).accept()
    assert NEW_MODEL in AdminPage(browser).models_names_in_list()
