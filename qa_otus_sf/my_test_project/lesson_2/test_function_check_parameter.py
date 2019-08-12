import requests


def test_url_status_code(url_param):
    """Проверяем ответ на 200"""
    res = requests.get(url_param)
    assert res.status_code == 200

