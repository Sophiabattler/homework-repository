"""Tests for task03 - Min&max"""
import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "file_name, mini, maxi",
    [
        ("./tests/homework1/test_task3_1.txt", -2000, 2000),
        ("./tests/homework1/test_task3_2.txt", 5, 5),
    ],
)
def test_min_max(file_name: str, mini: int, maxi: int):
    """Testing that file.txt will be read
    and min and max values will be returned
    as a tuple: for some lines, for one line"""
    assert find_maximum_and_minimum(file_name) == (mini, maxi)
