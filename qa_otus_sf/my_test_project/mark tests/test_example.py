import pytest

@pytest.mark.env('stage1')
def test_basic_db_operation():
    print('Test result')

@pytest.mark.env('stage1')
@pytest.mark.env('stage2')
def test_2_marks():
    print('Two marks')

#pytest test_example.py -E stage2
#pytest test_example.py -E stage1