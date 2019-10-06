import pytest
import requests
import allure


@pytest.mark.parametrize("test_data", ['dog', 'mad', 'almanac', 'brothers', 'goathouse'])
@allure.feature('Проверяем выдачу по ключевому слову в имени')
def test_one(test_data):
    """Проверяем выдачу по ключевому слову в имени"""
    response = requests.get('https://api.openbrewerydb.org/breweries?by_name=%s' % test_data)
    assert test_data in response.json()[0]['name'].lower()


@pytest.mark.parametrize("id_brewery, name", [(5494, 'MadTree Brewing'),
                                              (1, '5 Rivers Brewing LLC'),
                                              (999, 'Secret Trail Brewing Company, LLC')],
                         ids=["id=5494", "id=1", "id=999"])
def test_two(id_brewery, name):
    """Проверяем выдачу конкретной пивоварни по id"""
    response = requests.get('https://api.openbrewerydb.org/breweries/%s' % id_brewery)
    assert name == response.json()['name']


def test_three():
    """Проверяем фильтрацию по штату, сортировку по типу/имени"""
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=ohio&sort=type,-name')
    assert len(response.json()) == 20
    assert response.json()[0]['id'] == 5643
    assert response.json()[-1]['id'] == 5591


@pytest.mark.parametrize("pagination, max_per_page, first_result, last_result", [(2, 30, 410, 760),
                                                                                 (5, 10, 543, 654)])
def test_four(pagination, max_per_page, first_result, last_result):
    """Проверяем пагинацию и кол-во результатов"""
    response = requests.get('https://api.openbrewerydb.org/breweries?page=%s&per_page=%s'
                            % (pagination, max_per_page))
    assert len(response.json()) == max_per_page
    assert response.json()[0]['id'] == first_result
    assert response.json()[-1]['id'] == last_result


@pytest.mark.parametrize('ids', [('6662', '242', '3437', '3481', '3884', '4098', '4147',
                                  '372', '371', '3100', '4606', '1230', '1815', '1817', '1818')])
def test_five(ids):
    """Проверяем автозаполнение, что в выдае нужные нам id"""
    response = requests.get('https://api.openbrewerydb.org/breweries/autocomplete?query=big')
    assert len(response.json()) == 15
    for i in range(len(response.json())):
        assert response.json()[i]['id'] in ids
