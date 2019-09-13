from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Common, Admin, Catalog, Product, Main


def test_promoblock(browser):
    """Проверяем что по ссылке из промоблока открывается нужный нам товар"""
    browser.find_element_by_xpath(Main.promoblock).click()
    assert browser.find_element_by_xpath(Product.product_options_div_h1).text \
           == 'Samsung Galaxy Tab 10.1'


def test_add_item_to_cart(browser):
    """Добавляем в корзину три товара и проверяем что они отображаются"""
    browser.get('http://localhost/index.php?route=product/product&path=20_27&product_id=41')
    qty_items = browser.find_element_by_xpath(Product.available_options_qty_input)
    qty_items.clear()
    qty_items.send_keys('3')
    browser.find_element_by_xpath(Product.available_options_add_to_cart_button).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, Product.available_options_add_to_cart_button)))
    assert '3 item(s)' in \
           browser.find_element_by_xpath(Common.shopping_cart_total).text


def test_change_currency(browser):
    """Меняем валюту и проверяем что цена изменилась"""
    browser.get('http://localhost/index.php?route=product/product&path=34&product_id=48')
    assert browser.find_element_by_xpath(Product.product_options_div_h2_price).text == '$122.00'
    browser.find_element_by_xpath(Common.Header.currency).click()
    browser.find_element_by_xpath(Common.Header.currency_euro).click()
    assert browser.find_element_by_xpath(Product.product_options_div_h2_price).text == '95.72€'


def test_assert_sort(browser):
    """Меняем сортировку и проверяем что порядок выдачи изменился"""
    browser.get('http://localhost/index.php?route=product/category&path=18')
    assert 'HP LP3065' in browser.find_element_by_xpath(Common.product_item).text
    browser.find_element_by_xpath(Catalog.RefineSearch.sort_by_select).click()
    browser.find_element_by_xpath(Catalog.RefineSearch.sort_by_select_option_name_z_a).click()
    assert 'Sony VAIO' in browser.find_element_by_xpath(Common.product_item).text


def test_login(browser):
    """Логинимся и проверяем что нам становятся доступны заголовки внутри аккаунта"""
    browser.get('https://localhost/index.php?route=account/login')
    browser.find_element_by_xpath(Admin.email_input).send_keys('234@234.ru')
    browser.find_element_by_xpath(Admin.password_input).send_keys('123123')
    browser.find_element_by_xpath(Admin.button_submit).click()
    assert 'My Account', 'My Affiliate Account' in \
                         browser.find_elements_by_xpath(Admin.ClientAdminPage.Account.h2).text
