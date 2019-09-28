import os
import pytest
import logging
from datetime import date
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener


@pytest.fixture(scope='session', autouse=True)
def proxy():
    server = Server(os.path.join(os.path.dirname(__file__), 'browsermob-proxy-2.1.4/bin/browsermob-proxy'))
    server.start()
    proxy = server.create_proxy()
    proxy.new_har(title='project_har')
    yield proxy
    server.stop()


@pytest.fixture(scope='session', autouse=True)
def driver(request, logger, proxy):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--start-fullscreen')
        options.add_argument(f'--proxy-server={proxy.proxy}')
        options.add_experimental_option('w3c', False)
        caps = DesiredCapabilities.CHROME.copy()
        caps['timeouts'] = {'implicit': 20000, 'pageLoad': 20000, 'script': 20000}
        caps['loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
        wd = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=caps),
                                  BaseListener(logger))
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        caps = DesiredCapabilities.FIREFOX.copy()
        caps['timeouts'] = {'implicit': 25000, 'pageLoad': 25000, 'script': 25000}
        wd = EventFiringWebDriver(webdriver.Firefox(options=options, desired_capabilities=caps,
                                                    proxy=proxy.proxy),
                                  BaseListener(logger))
        wd.maximize_window()
    else:
        raise ValueError('Unsupported browser.')
    yield wd
    wd.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', help='Supported browsers: chrome, firefox', default='chrome')


@pytest.fixture(scope='session', autouse=True)
def logger():
    logger = MyLogger(name='session_logger').launch_logger()
    yield logger
    logging.shutdown()


class BaseListener(AbstractEventListener):

    def __init__(self, logger):
        self.logger = logger

    def on_exception(self, exception, driver):
        driver.save_screenshot(f'{driver.current_url}-{driver.name}{date.today()}.png')
        self.logger.error(exception)

    def before_navigate_to(self, url, driver):
        self.logger.info(f'\n WebDriver log - Going to {url}')

    def after_navigate_to(self, url, driver):
        self.logger.info(f'\nWebDriver log - Opened {url}')


class MyLogger:

    def __init__(self, name):
        self.name = name

    def launch_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_log.setFormatter(console_format)
        logger.addHandler(console_log)
        return logger