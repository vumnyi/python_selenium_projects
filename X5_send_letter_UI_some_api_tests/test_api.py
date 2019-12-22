import requests
import pytest


def test_anwser_from_get_test_api():
    answer = {
        "name": "testName",
        "count": 1,
        "priority": True
    }
    response = requests.get('http://localhost:8080/test-api')
    assert response.status_code == 200
    for key in answer:
        assert answer[key] == response.json()[0][key]


@pytest.mark.parametrize('ids', [(1), (9), (11), (99), (100)])
def test_anwser_from_post_test_api_id(ids):
    response = requests.post(f'http://localhost:8080/test-api/{ids}', data={'test': 'auto', 'log': True})
    assert response.status_code == 200
    assert response.json()["testId"] == ids


def test_anwser_from_post_test_api_id_null(ids):
    response = requests.post(f'http://localhost:8080/test-api/null', data={'test': 'auto', 'log': True})
    assert response.status_code == 404
