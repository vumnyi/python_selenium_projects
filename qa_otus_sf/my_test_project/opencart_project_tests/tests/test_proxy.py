from browsermobproxy import Server
import pytest
import urllib.parse
from selenium import webdriver

server = Server("/home/sergey/repositories/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()
proxy.new_har()


@pytest.fixture
def chrome_browser(request):
    chrome_options = webdriver.ChromeOptions()
    url = urllib.parse.urlparse(proxy.proxy).path
    chrome_options.add_argument('--proxy-server=%s' % url)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    request.addfinalizer(driver.quit)
    return driver


def test_proxy(chrome_browser):
    chrome_browser.get('https://otus.ru/')
    print(' ')
    print(proxy.har)
    print(proxy.har['log']['creator'])
