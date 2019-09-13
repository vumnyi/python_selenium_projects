from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
from locators import Admin, Common


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your url")
    parser.addoption("--options", "-O", action="store", default="", help="choose headless")
    parser.addoption("--iwait", "--IW", action="store", default="0", help="choose implicitly wait")


@pytest.fixture(scope='session')
def browser(request):
    browser_param = request.config.getoption("--browser")
    browser_options = request.config.getoption("--options")
    if browser_param == "chrome":
        if browser_options == 'headless':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
    elif browser_param == "firefox":
        if browser_options == 'headless':
            options = Options()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
        else:
            driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.fixture()
def admin_autorization(browser):
    browser.get('https://localhost/admin/')
    browser.find_element_by_xpath(Admin.username_input).send_keys('user')
    browser.find_element_by_xpath(Common.password_input).send_keys('bitnami1')
    browser.find_element_by_xpath(Common.button_submit).click()
    assert browser.find_element_by_xpath('//h1').text == 'Dashboard'


@pytest.fixture()
def client_autorization(browser):
    browser.get('https://localhost/index.php?route=account/login')
    browser.find_element_by_xpath(Common.email_input).send_keys('234@234.ru')
    browser.find_element_by_xpath(Common.password_input).send_keys('123123')
    browser.find_element_by_xpath(Common.button_submit).click()
    assert browser.find_element_by_xpath('//h2').text == 'My Account'
