from selenium import webdriver
from application import *
import pytest
import requests


@pytest.fixture()
def check_google_host_is_ok():
    r = requests.get('https://accounts.google.com/signin')
    return r.ok

@pytest.fixture()
def autorization(browser):
    email, password = 'auto.python.ep@gmail.com', 'automationPython13'
    Application(browser).go_to_gmail()\
        .send_to_locator_value("//input[@type='email']", email)\
        .send_to_locator_value("//input[@type='password']", password)
    assert 'Добро пожаловать' in browser.find_element_by_xpath('//h1').text

@pytest.fixture()
def logout(browser):
    Application(browser).click_by_locator('//a[contains(@aria-label, "Аккаунт")]')\
        .click_by_locator('//a[text() = "Выйти"]')
    assert 'Выберите аккаунт' in browser.find_element_by_xpath('//h1/span').text

@pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture()
def browser(request, check_google_host_is_ok):
    if check_google_host_is_ok:
        # browser = webdriver.Chrome('./chromedriver')
        browser_param = request.param
        capabilities = {
            'chrome': {
                "browserName": "chrome",
                "version": "78.0",
                "enableVNC": True,
                "enableVideo": False
            },
            'firefox': {
                "browserName": "firefox",
                "version": "71.0",
                "enableVNC": True,
                "enableVideo": False
            }
        }
        browser = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities.get(browser_param))
            # desired_capabilities = {
            #     "browserName": "chrome",
            #     "version": "78.0",
            #     "enableVNC": True,
            #     "enableVideo": False
            # })
        browser.implicitly_wait(5)
        browser.maximize_window()
        request.addfinalizer(browser.quit)
        return browser
    else:
        raise Exception('Server non-200 return code')

