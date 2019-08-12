import requests
import pytest


@pytest.mark.parametrize('userId, name, email, website',
                         [('5', 'Chelsey Dietrich', 'Lucio_Hettinger@annie.ca', 'demarco.info'),
                          ('9', 'Glenna Reichert', 'Chaim_McDermott@dana.io', 'conrad.com')])
def test_one(userId, name, email, website):
    """Получаем пользователя с определенным id"""
    res = requests.get('https://jsonplaceholder.typicode.com/users/%s' % userId)
    assert res.json()['name'] == name
    assert res.json()['email'] == email
    assert res.json()['website'] == website



@pytest.mark.parametrize('path, count',
                         [('posts', 100),
                          ('comments', 500),
                          ('albums', 100),
                          ('photos', 5000),
                          ('todos', 200),
                          ('users', 10)])
def test_two(path, count):
    """Проверяем количество выдаваемых данных по путям"""
    res = requests.get('https://jsonplaceholder.typicode.com/%s' % path)
    assert len(res.json()) == count


@pytest.mark.parametrize('ids', [(1), (9), (11), (99), (100)])
def test_three(ids):
    """Получаем комментарии к посту"""
    response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=%s' % ids)
    assert response.json()[0]['postId'] == ids
    assert response.json()[0]['email'] != []


def test_four():
    """Проверяем что при запросе по неверному path отдаёт 404"""
    res = requests.get('https://jsonplaceholder.typicode.com/TEST')
    assert res.status_code == 404


@pytest.mark.parametrize('user_id, count', [(9, 10)])
def test_five(user_id, count):
    """Получаем посты определенного юзера"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=%s' % user_id)
    assert len(response.json()) == count
    for i in response.json():
        assert i['userId'] == user_id
