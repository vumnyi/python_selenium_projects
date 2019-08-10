import pytest
import math


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\nHello from {request.scope} fixture!")

    def fin():
        print(f"\nFinalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\nHello from {request.scope} fixture!")

    def fin():
        print(f"\nFinalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope='session')
def fixture_return_string():
    return 'Python QA Engineer | OTUS'


@pytest.fixture(params=[0, 1, 9, 11])
def fixture_check_type(request):
    return request.param


@pytest.fixture()
def fixture_dict():
    return {'1': 'one', '2': 'two'}


@pytest.fixture()
def fixture_for_request(request):
    def fin():
        print("\nThis is finalizer after test")
        print('SCOPE=' + request.scope)

    request.addfinalizer(fin)


@pytest.fixture()
def fixture_return_set():
    return set('hello')


@pytest.fixture()
def fixture_list_comprehensions():
    return [i for i in range(20) if i % 2 == 0]


@pytest.fixture()
def fixture_tuple_as_a_key():
    return {'1': 'string', (1, 2, 3): 'tuple'}


@pytest.fixture()
def fixture_set_difference():
    s1, s2 = {1, 2, 3, 4}, {3, 4, 5, 6}
    return s1.difference(s2)


@pytest.fixture()
def fixture_return_math_module():
    return math


@pytest.fixture(scope="module")
def fixture_upper():
    return 'test'.upper()


@pytest.fixture(scope="module")
def fixture_multiply():
    return 5 * 5
