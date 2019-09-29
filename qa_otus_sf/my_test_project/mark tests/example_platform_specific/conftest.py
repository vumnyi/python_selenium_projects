import sys
import pytest

ALL = set('darwin linux win'.split())


def pytest_runtest_setup(item):
    supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
    plat = sys.platform
    if supported_platforms and plat not in supported_platforms:
        pytest.skip('cannot run platform %s' % plat)
