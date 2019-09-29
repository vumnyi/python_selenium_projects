import pytest


@pytest.mark.darwin
def test_if_apple_is_evil():
    pass


@pytest.mark.linux
def test_if_linux_works():
    pass


@pytest.mark.win
def test_if_win_crashes():
    pass


def test_runs_everywhere():
    pass

# pytest test_platform_specific.py -m linux
# pytest test_platform_specific.py
