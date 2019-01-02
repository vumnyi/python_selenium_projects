from selenium_fixture import *
from application import *


def test_login(app):
    app.go_to_gmail()
    app.switch_language()
    app.autorization('auto.python.ep@gmail.com', 'automationPython13')
    assert 'имя фамилия' in app.driver.find_element_by_xpath('//h1').text

def test_recovery_password(app):
    app.go_to_gmail()
    app.recovery_password('auto.python.ep@gmail.com')
    assert 'An email with a verification code was just sent to test@test.com' in app.driver.find_element_by_css('span.TQGan').text




