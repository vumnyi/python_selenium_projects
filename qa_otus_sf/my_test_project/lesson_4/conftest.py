from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome")
    parser.addoption("--url", "-U", action="store", default="http://localhost/")



@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.fixture(params=["chrome", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()


    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))
    return driver