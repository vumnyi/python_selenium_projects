from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your url")
    parser.addoption("--options", "-O", action="store", default="", help="choose headless")


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

    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver
