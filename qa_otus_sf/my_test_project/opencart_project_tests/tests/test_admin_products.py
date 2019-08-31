"""Tests for Products page"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from locators import AdminPage, ProductPage

PRODUCT_NAME = 'TESLA'
MODEL = 'MODEL S'
NEW_MODEL = 'ROADSTER'


def test_add_item(browser, admin_autorization):
    """Добавляем новый продукт в админке, используем фикстуру
     для авторизации в админке, проверяем что наш продукт в списке"""
    browser.find_element_by_xpath(AdminPage.AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(AdminPage.AdminNavigation.sections_item('Products')).click()
    assert browser.find_element_by_xpath('//h1').text == 'Products'
    browser.find_element_by_xpath(AdminPage.AdminButtonsEditItem.add_new).click()
    browser.find_element_by_xpath(AdminPage.AddProduct.
                                  General.product_name_input).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(AdminPage.AddProduct.
                                  General.meta_tag_title).send_keys('TESLA TEST')
    browser.find_element_by_xpath(AdminPage.AddProduct.
                                  topics('Data')).click()
    browser.find_element_by_xpath(AdminPage.AddProduct.
                                  Data.model_input).send_keys(MODEL)
    browser.find_element_by_xpath(AdminPage.AddProduct.
                                  Data.price_input).send_keys('45000')
    quantity = browser.find_element_by_xpath(AdminPage.
                                             AddProduct.Data.quantity_input)
    quantity.clear()
    quantity.send_keys('13')
    browser.find_element_by_xpath(AdminPage.AdminButtonsEditItem.save_button).click()
    browser.find_element_by_xpath(AdminPage.AdminFilter.product_name_input).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(AdminPage.AdminFilter.model_name_input).send_keys(MODEL)
    browser.find_element_by_xpath(AdminPage.AdminFilter.filter_button).click()
    parse_product_names = browser.find_elements_by_xpath(AdminPage.ProductList.product_names)
    try:
        assert PRODUCT_NAME in [i.text for i in parse_product_names]
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + PRODUCT_NAME)


def test_edit_item(browser, admin_autorization):
    """Редактируем продукт в админке (меняем модель), используем фикстуру
     для авторизации в админке, провеярем что новая модель в списке"""
    browser.find_element_by_xpath(AdminPage.AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(AdminPage.AdminNavigation.sections_item('Products')).click()
    browser.find_element_by_xpath(AdminPage.AdminFilter.product_name_input).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(AdminPage.AdminFilter.filter_button).click()
    browser.find_element_by_xpath(AdminPage.AdminButtonsEditItem.edit_button).click()
    browser.find_element_by_xpath(AdminPage.AddProduct.topics('Data')).click()
    model_old = browser.find_element_by_xpath(AdminPage.AddProduct.Data.model_input)
    model_old.clear()
    model_old.send_keys(NEW_MODEL)
    browser.find_element_by_xpath(AdminPage.AdminButtonsEditItem.save_button).click()
    parse_product_models = browser.find_elements_by_xpath(AdminPage.ProductList.product_models)
    try:
        assert NEW_MODEL in [i.text for i in parse_product_models]
    except AssertionError as error:
        print(error)
        print('\nНе найдено ' + NEW_MODEL)


def test_delete_item(browser, admin_autorization):
    """Удаляем продукт в админке, используем фикстуру
    для авторизации в админке, проверяем что новая модель не в списке"""
    browser.find_element_by_xpath(AdminPage.
                                  AdminNavigation.sections('Catalog')).click()
    browser.find_element_by_xpath(AdminPage.
                                  AdminNavigation.sections_item('Products')).click()
    browser.find_element_by_xpath(AdminPage.
                                  AdminFilter.product_name_input).send_keys(PRODUCT_NAME)
    browser.find_element_by_xpath(AdminPage.
                                  AdminFilter.filter_button).click()
    browser.find_element_by_xpath(AdminPage.
                                  ProductList.current_product_check_box(NEW_MODEL)).click()
    browser.find_element_by_xpath(AdminPage.
                                  AdminButtonsEditItem.delete_button).click()
    Alert(browser).accept()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, ProductPage.Alert.success)))
    parse_product_models = browser.find_elements_by_xpath(AdminPage.ProductList.product_models)
    assert NEW_MODEL not in [i.text for i in parse_product_models]
