from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest
from locators import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your url")
    parser.addoption("--options", "-O", action="store", default="", help="choose headless")
    parser.addoption("--iwait", "--IW", action="store", default="0", help="choose implicitly wait")


@pytest.fixture(scope='session')
def browser(request):
    browser_param = request.config.getoption("--browser")
    browser_options = request.config.getoption("--options")
    browser_imp_wait = request.config.getoption("--iwait")
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
    if browser_imp_wait:
        driver.implicitly_wait(browser_imp_wait)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver


# #УЗНАТЬ КАК ПЕРЕДАВАТЬ ЛОГИН/ПАРОЛЬ В ФИКСТУРУ ИЗ ТЕСТА
@pytest.fixture()
def admin_autorization(browser):
    browser.get('https://localhost/admin/')
    browser.find_element_by_xpath(AdminPage.username_input).send_keys('user')
    browser.find_element_by_xpath(AdminPage.password_input).send_keys('bitnami1')
    browser.find_element_by_xpath(AdminPage.button_submit).click()
    browser.find_element_by_xpath('//h1').text == 'Dashboard'
