
import pytest

@pytest.fixture
def with_addfinalizer(request):
    print("\nStart addfinalizer fixture")
    def fin():
        print("\nFinalize addfinalizer fixture")
    request.addfinalizer(fin)
    s = []
    return s[1]

@pytest.fixture
def with_yield():
    print("\nStart yield fixture")
    s = []
    yield s[1]
    print("\nFinalize yield fixture")

def test_one(with_yield):
    pass

# def test_two(with_addfinalizer):
#     pass