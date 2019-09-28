from selenium import webdriver
import pytest


# запуск сервера
#:~/repositories/pythonREP/qa_otus_sf/my_test_project/opencart_project_tests$ java -jar selenium-server-standalone-3.141.59.jar
# запуск сервера как хаба
# java -jar selenium-server-standalone-3.141.59.jar -role hub
# запуск ноды
# java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://172.17.0.1:4444/grid/register/
# разные инстансы
# java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://172.17.0.1:4444/grid/register/ -capabilities browserName=chrome,maxInstances=2 -capabilities browserName=firefox,maxInstances=1


@pytest.fixture
def browser(request):
    wd = webdriver.Remote("http://localhost:4444/wd/hub",
                          desired_capabilities={'browserName': 'chrome', 'version': '', 'platform': 'ANY'})

    request.addfinalizer(wd.quit)
    return wd


def test_grid(browser):
    browser.get("http://www.google.com")
    if not "Google" in browser.title:
        raise Exception("Unable to load google page!")
    elem = browser.find_element_by_name("q")
    elem.click()
