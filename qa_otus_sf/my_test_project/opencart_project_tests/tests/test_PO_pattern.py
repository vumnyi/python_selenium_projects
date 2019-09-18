from page_objects import MainPage, ProductPage, UserPage
from page_objects.common.YourStoreBlock import YourStoreBlock
from page_objects.common.Headings import Headings
from page_objects.common import TestUsers


def test_write_a_review(parametrize_browser):
    """Проверяем что можно оставить отзыв о товаре, через фикстуру передаем
    параметры запуска теста в двух разных браузерах"""
    browser = parametrize_browser
    browser.get('https://localhost/')
    MainPage(browser).click_featured_product(2)
    ProductPage(browser).click_tab_item('Reviews') \
        .review_input('name', 'This is TEST NAME') \
        .review_input('review', 'This is a text message for review') \
        .choose_product_rating('5')
    MainPage(browser).click_button('Continue')
    assert 'Thank you for your review. It has been submitted to the webmaster for approval.' \
           in ProductPage(browser).get_alert_text()


def test_search_product(browser):
    """Проверяем что через поиск можем найти нужный нам товар"""
    browser.get('https://localhost/')
    YourStoreBlock(browser).search_input_text_and_click('Canon')
    MainPage(browser).click_featured_product(1)
    assert 'Canon EOS 5D' == Headings(browser).get_h1_text(2)


def test_change_user_password(browser, client_autorization):
    """Проверяем возможность изменить пароль"""
    browser.get('https://localhost/index.php?route=account/password')
    UserPage(browser).input_field_name('Password', 'test')
    UserPage(browser).input_field_name('Confirm', 'test')
    UserPage(browser).click_button_continue()
    assert 'Success: Your password has been successfully updated.' \
           in ProductPage(browser).get_alert_text()
    UserPage(browser).my_account_dropdown('Logout')
    browser.get('https://localhost/index.php?route=account/login')
    UserPage(browser).login_user(email=TestUsers.user1['email'], password='test')
    # меняю пароль на старый
    browser.get('https://localhost/index.php?route=account/password')
    UserPage(browser).change_password(TestUsers.user1['password'])
