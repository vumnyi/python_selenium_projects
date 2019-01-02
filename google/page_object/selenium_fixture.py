import pytest
from application import *


@pytest.fixture()
def app(request):
    driver = webdriver.Chrome(r'C:\Python36\GitLAB_pythonREP\tests\chromedriver.exe')
    def close_driver():
        driver.quit()
    request.addfinalizer(close_driver)
    return Application(driver)



