import pytest
from application import *
import allure


# https://www.cnews.ru/news/top/2019-12-16_google_blokiruet_populyarnye


@allure.story('Отправка писем')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Параметризованный тест')
@pytest.mark.parametrize("email, topic, body",
                         [('test_letter@mail.ru', 'Тестовое письмо', 'Какой то текст 12345'),
                          ('test_letter2345@mail.ru', 'Письмо без тела', ''),
                          ('test_letter001@mail.ru', '', 'Письмо без темы')],
                         ids=['Тестовое письмо', 'Письмо без тела', 'Письмо без темы'])
def test_send_letter(browser, autorization, email, topic, body):
    Application(browser).send_letter(email=email, topic=topic, body=body)
    assert browser.find_element_by_xpath("//span[text() = 'Письмо отправлено.']")
