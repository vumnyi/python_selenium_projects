from page_objects import MainPage, UserPage, ProductPage, CartPage, CatalogPage
from page_objects.common.YourStoreBlock import YourStoreBlock
from page_objects.common.TopMenu import TopMenu
from page_objects.common import TestUsers


def test_promoblock(browser):
    """Проверяем что по ссылке из промоблока открывается нужный нам товар"""
    MainPage(browser).click_promoblock()
    assert ProductPage(browser).get_h1_text() == 'Samsung Galaxy Tab 10.1'


def test_add_item_to_cart(browser):
    """Добавляем в корзину три товара и проверяем что они отображаются"""
    browser.get('http://localhost/index.php?route=product/product&path=20_27&product_id=41')
    ProductPage(browser).how_much_items_input(3).click_add_to_cart_btn()
    ProductPage(browser).verify_add_to_cart_btn_clickable()
    assert '3 item(s)' in YourStoreBlock(browser).get_cart_button_text()


def test_change_currency(browser):
    """Меняем валюту и проверяем что цена изменилась"""
    browser.get('http://localhost/index.php?route=product/product&path=34&product_id=48')
    assert ProductPage(browser).get_price_text() == '$122.00'
    TopMenu(browser).change_currency('euro')
    assert ProductPage(browser).get_price_text() == '95.72€'


def test_assert_sort(browser):
    """Меняем сортировку и проверяем что порядок выдачи изменился"""
    browser.get('http://localhost/index.php?route=product/category&path=18')
    assert 'HP LP3065' in MainPage(browser).featured_product_name(1)
    CatalogPage(browser).change_sort('name_z_a')
    assert 'Sony VAIO' in MainPage(browser).featured_product_name(1)


def test_login(browser):
    """Логинимся и проверяем что нам становятся доступны заголовки внутри аккаунта"""
    browser.get('https://localhost/index.php?route=account/login')
    UserPage(browser).login_user(email=TestUsers.user1['email'], password=TestUsers.user1['password'])
    assert 'My Account', 'My Affiliate Account' in UserPage(browser).get_h2_text()
