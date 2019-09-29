from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import pytest
from browsermobproxy import Server
from locators import Admin, Common
import logging
from datetime import date
import platform


@pytest.fixture(scope='session', autouse=True)
# https://automated-testing.info/t/chto-takoe-browsermob-proxy-i-kak-zastavit-ego-rabotat-tutorial-dlya-nachinayushhih-primer-ispolzovaniya-na-python/3510
# https://automated-testing.info/t/wd-python-kak-pojmat-get-zapros/1905
def proxy():
    server = Server("/home/sergey/repositories/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()
    proxy.new_har(title='project_har')
    yield proxy
    server.stop()


class MyListener(AbstractEventListener):
    logging.basicConfig(filename='data.log', filemode='w', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def before_find(self, by, value, driver):
        logging.info('Try to find element ' + str(value))

    def before_click(self, element, driver):
        logging.info('Try to click element with class: ' + str(element.get_attribute('class')))

    def on_exception(self, exception, driver):
        driver.save_screenshot(f'screenshots/{driver.name} {date.today()}.png')
        logging.info('SCREENSHOT TAKEN')
        logging.error(exception)


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost/", help="choose your url")
    parser.addoption("--options", "-O", action="store", default="", help="choose headless")


@pytest.fixture(scope='session', autouse=True)
def browser(request, proxy):
    browser_param = request.config.getoption("--browser")
    browser_options = request.config.getoption("--options")
    if browser_param == "chrome":
        if browser_options == 'headless':
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.ChromeOptions()
            # options.add_argument(f'--proxy-server={proxy.proxy}')
            driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())

    elif browser_param == "firefox":
        if browser_options == 'headless':
            options = Options()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
        else:
            driver = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    driver.implicitly_wait(5)
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
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.get(request.config.getoption("--url"))
    return driver


@pytest.mark.usefixtures('environment_info')
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {'browser': request.config.getoption('--browser'),
         'address': request.config.getoption('--url'),
         'env_info': environment_info[0],  # os_platform
         'platform_machine': environment_info[2],
         'python_version': environment_info[3],
         'example': "Hello, it's EXAMPLE"}
    )
    yield


@pytest.fixture(scope='session')
def environment_info():
    # settings environment in html-report
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    platform_machine = platform.machine()
    python_version = platform.python_version()
    return os_platform, linux_dist, platform_machine, python_version


@pytest.fixture()
def admin_autorization(browser):
    browser.get('https://localhost/admin/')
    browser.find_element_by_xpath(Admin.username_input["xpath"]).send_keys('user')
    browser.find_element_by_xpath(Common.password_input["xpath"]).send_keys('bitnami1')
    browser.find_element_by_xpath(Common.button_submit["xpath"]).click()
    assert browser.find_element_by_xpath('//h1').text == 'Dashboard'
    for i in browser.get_log('browser'):
        print(i)


@pytest.fixture()
def client_autorization(browser):
    browser.get('https://localhost/index.php?route=account/login')
    browser.find_element_by_xpath(Common.email_input["xpath"]).send_keys('234@234.ru')
    browser.find_element_by_xpath(Common.password_input["xpath"]).send_keys('123123')
    browser.find_element_by_xpath(Common.button_submit["xpath"]).click()
    assert browser.find_element_by_xpath('//h2').text == 'My Account'
