import pytest


@pytest.fixture(params=['boston', 'english', 'french'])
def fixture_with_params(request):
    return request.param


def pytest_addoption(parser):
    """Парсим опцию"""
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture
def url_param(request):
    """Возвращаем опцию"""
    return request.config.getoption("--url")
