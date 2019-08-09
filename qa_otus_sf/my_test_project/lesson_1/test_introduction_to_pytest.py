def test_one(fixture_return_string):
    """Проверяем наличие слова в строке"""
    print('\nAssert "OTUS" in string')
    assert 'OTUS' in fixture_return_string


def test_two(fixture_check_type):
    """Проверяем тип данных"""
    print('\nAssert type with param', fixture_check_type)
    assert True == (type(fixture_check_type) is int)


def test_three(fixture_dict, fixture_for_request):
    """Проверяем наличие значения по ключу"""
    print('\nAssert key = 2 value = two, DICT:', fixture_dict)
    assert fixture_dict['2'] == 'two'


def test_four(fixture_return_set):
    """Проверяем длину множества"""
    print('\nAssert len set("hello") == 4')
    assert len(fixture_return_set) == 4


def test_five(fixture_list_comprehensions):
    """Проверяем четность чисел в списке"""
    print('\nAssert even number in list comprehensions')
    for i in fixture_list_comprehensions:
        assert i % 2 == 0


def test_six(fixture_tuple_as_a_key):
    """Проверяем возможность использования кортежа как ключа"""
    print('\nAssert tuple as a key')
    assert fixture_tuple_as_a_key[(1, 2, 3)] == 'tuple'


def test_seven(fixture_set_difference):
    """Проверяем на разность множество"""
    print('\nAssert set difference')
    assert fixture_set_difference == {1, 2}


def test_eight(fixture_return_math_module, session_fixture):
    """Проверяем возможность импорта модуля math"""
    print('\nAssert import math module')
    assert fixture_return_math_module.pi == 3.141592653589793


def test_nine(fixture_upper):
    """Проверяем возвращение строки в верхнем регистре"""
    print('\nAssert return upper string')
    assert fixture_upper == 'TEST'


def test_ten(fixture_multiply, module_fixture):
    """Проверяем базовую операцию умножения"""
    print('\nAssert 5*5 == 25')
    assert fixture_multiply == 25
