import requests
import pytest


@pytest.mark.parametrize("test_data", ['beagle', 'bulldog', 'pointer', 'schnauzer', 'wolfhound'])
def test_one(test_data):
    """Проверяем успешный код ответа c разными породами из параметров"""
    response = requests.get('https://dog.ceo/api/breed/%s/images/random' % test_data)
    assert response.status_code == 200


def test_two(fixture_with_params):
    """Проверяем статус ответа группы одной породы с параметрами из фикстуры"""
    response = requests.get('https://dog.ceo/api/breed/bulldog/%s/images/random'
                            % fixture_with_params)
    assert response.json()['status'] == 'success'


def test_three():
    """Проверяем количество пород"""
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert len(response.json()['message']) == 87


def test_four():
    """Проверяем кодировку ответа"""
    response = requests.get('https://dog.ceo/dog-api')
    assert response.headers['Content-Encoding'] == 'gzip'


def test_five():
    """Проверяем на ошибку Breed not found (master breed does not exist)
     при передаче TEST в запросе"""
    response = requests.get('https://dog.ceo/api/breed/TEST/english/images/random')
    assert response.json()['status'] == 'error'
    assert response.json()['message'] == 'Breed not found (master breed does not exist)'
