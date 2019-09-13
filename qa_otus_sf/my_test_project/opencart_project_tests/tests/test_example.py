from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Common, Main, Product, Admin
from page_objects import MainPage, UserPage, ProductPage, CartPage
from page_objects.common import AlertMenu, TestUsers
import time


def test_add_to_wish_list(browser):
    browser.get('https://localhost/')
    product_name = MainPage(browser).featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_wish_list()
    AlertMenu.AlertDialog(browser).click_login()
    UserPage(browser).login_user(email=TestUsers.user1['email'], password=TestUsers.user1['password']). \
        open_right_menu_item('Wish List'). \
        verify_product(product_name).my_account_dropdown('Logout')


def test_add_to_cart(browser):
    browser.get('https://localhost/')
    product_name = MainPage(browser).featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser).add_to_cart()
    AlertMenu.AlertDialog(browser).click_to_cart()
    CartPage(browser).verify_product(product_name). \
        click_button_name('Checkout')
    UserPage(browser).login_user(email=TestUsers.user1['email'], password=TestUsers.user1['password']). \
        verify_payment_form()
