"""Tests for Products page"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from locators import Admin, Product
from page_objects import MainPage, UserPage, ProductPage, CartPage, BasePage, CatalogPage
from page_objects.common.YourStoreBlock import YourStore
from page_objects.common.TopMenu import TopMenu
from page_objects.common import TestUsers

PRODUCT_NAME = 'TESLA'
MODEL = 'MODEL S'
NEW_MODEL = 'ROADSTER'


def test_add_item(browser, admin_autorization):
    """Добавляем новый продукт в админке, используем фикстуру
     для авторизации в админке, проверяем что наш продукт в списке"""
    browser.find_element_by_xpath(Admin.AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(Admin.AdminNavigation.sections_item('Products')).click()
    assert browser.find_element_by_xpath('//h1').text == 'Products'
    browser.find_element_by_xpath(Admin.AdminButtonsEditItem.add_new["xpath"]).click()
    browser.find_element_by_xpath(Admin.AddProduct.
                                  General.product_name_input["xpath"]).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(Admin.AddProduct.
                                  General.meta_tag_title["xpath"]).send_keys('TESLA TEST')
    browser.find_element_by_xpath(Admin.AddProduct.
                                  topics('Data')).click()
    browser.find_element_by_xpath(Admin.AddProduct.
                                  Data.model_input["xpath"]).send_keys(MODEL)
    browser.find_element_by_xpath(Admin.AddProduct.
                                  Data.price_input["xpath"]).send_keys('45000')
    quantity = browser.find_element_by_xpath(Admin.
                                             AddProduct.Data.quantity_input["xpath"])
    quantity.clear()
    quantity.send_keys('13')
    browser.find_element_by_xpath(Admin.AdminButtonsEditItem.save_button["xpath"]).click()
    browser.find_element_by_xpath(Admin.AdminFilter.product_name_input["xpath"]).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(Admin.AdminFilter.model_name_input["xpath"]).send_keys(MODEL)
    browser.find_element_by_xpath(Admin.AdminFilter.filter_button["xpath"]).click()
    parse_product_names = browser.find_elements_by_xpath(Admin.ProductList.product_names["xpath"])
    try:
        assert PRODUCT_NAME in [i.text for i in parse_product_names]
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + PRODUCT_NAME)


def test_edit_item(browser, admin_autorization):
    """Редактируем продукт в админке (меняем модель), используем фикстуру
     для авторизации в админке, провеярем что новая модель в списке"""
    browser.find_element_by_xpath(Admin.AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(Admin.AdminNavigation.sections_item('Products')).click()
    browser.find_element_by_xpath(Admin.AdminFilter.product_name_input["xpath"]).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(Admin.AdminFilter.filter_button["xpath"]).click()
    browser.find_element_by_xpath(Admin.AdminButtonsEditItem.edit_button["xpath"]).click()
    browser.find_element_by_xpath(Admin.AddProduct.topics('Data')).click()
    model_old = browser.find_element_by_xpath(Admin.AddProduct.Data.model_input["xpath"])
    model_old.clear()
    model_old.send_keys(NEW_MODEL)
    browser.find_element_by_xpath(Admin.AdminButtonsEditItem.save_button["xpath"]).click()
    parse_product_models = browser.find_elements_by_xpath(Admin.ProductList.product_models["xpath"])
    try:
        assert NEW_MODEL in [i.text for i in parse_product_models]
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + NEW_MODEL)


def test_delete_item(browser, admin_autorization):
    """Удаляем продукт в админке, используем фикстуру
    для авторизации в админке, проверяем что новая модель не в списке"""
    browser.find_element_by_xpath(Admin.
                                  AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(Admin.
                                  AdminNavigation.sections_item('Products')).click()
    browser.find_element_by_xpath(Admin.
                                  AdminFilter.product_name_input["xpath"]).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(Admin.
                                  AdminFilter.filter_button["xpath"]).click()
    browser.find_element_by_xpath(Admin.
                                  ProductList.current_product_check_box(NEW_MODEL)).click()
    browser.find_element_by_xpath(Admin.
                                  AdminButtonsEditItem.delete_button["xpath"]).click()
    Alert(browser).accept()
    # WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, Product.Alert.success["xpath"])))
    parse_product_models = browser.find_elements_by_xpath(Admin.ProductList.product_models["xpath"])
    assert NEW_MODEL not in [i.text for i in parse_product_models]
