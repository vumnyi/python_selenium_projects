from page_objects import MainPage, UserPage, ProductPage, CartPage
from page_objects.common import TestUsers
from page_objects.common.AlertMenu import AlertDialog



def test_add_to_wish_list(browser):
    browser.get('https://localhost/')
    product_name = MainPage(browser).featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wish_list()
    AlertDialog(browser).click_login()
    UserPage(browser).login_user(email=TestUsers.user1['email'], password=TestUsers.user1['password']). \
        open_right_menu_item('Wish List'). \
        verify_product(product_name).my_account_dropdown('Logout')


def test_add_to_cart(browser):
    browser.get('https://localhost/')
    product_name = MainPage(browser).featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    AlertDialog(browser).click_to_cart()
    CartPage(browser).verify_product(product_name). \
        click_button_name('Checkout')
    UserPage(browser).login_user(email=TestUsers.user1['email'], password=TestUsers.user1['password']). \
        verify_payment_form()
