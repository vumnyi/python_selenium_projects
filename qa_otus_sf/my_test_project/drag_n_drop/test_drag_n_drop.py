from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_drag_n_drop():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get("https://code.makery.ch/library/dart-drag-and-drop/")
    driver.execute_script("window.scrollTo(0, 500);")
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to.frame(iframe)
    images = driver.find_elements_by_xpath("//*[@class='trash']/following-sibling::img")
    trash = driver.find_element_by_xpath("//*[@class='trash']")
    for i in images:
        actions.drag_and_drop(i, trash).perform()
    assert len(driver.find_elements_by_xpath("//*[@class='trash']/following-sibling::img")) == 0

    driver.quit()
