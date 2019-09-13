import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Admin, Product


# рипт для создания формы для загрузки файла
# browser.execute_script("""
#     var f = document.createElement("form");
#     f.id = "form-upload";
#     f.style.display = "block";
#     f.enctype = "multipart/form-data";
#     inp = document.createElement("input");
#     inp.type = "file";
#     inp.name = "file";
#     f.appendChild(inp);
#     body = document.getElementsByTagName("body")[0];
#     body.insertBefore(f, body.firstChild);
# """)


def test_upload_file(browser, admin_autorization):
    """Загружаем файл"""
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'test_img.png')
    browser.find_element_by_xpath(Admin.AdminNavigation.sections('Catalog')).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, Admin.AdminNavigation.sections_item('Downloads'))))
    browser.find_element_by_xpath(Admin.AdminNavigation.sections_item('Downloads')).click()
    browser.find_element_by_xpath(Admin.AdminButtonsEditItem.add_new).click()
    #выполняем клик через js чтобы в DOM появилась форма для загрузки
    browser.execute_script("document.getElementById('button-upload').click()")
    browser.find_element_by_xpath("//input[@type='file']").send_keys(filename)
    WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    assert "Your file was successfully uploaded!" in alert_text
    alert.accept()
