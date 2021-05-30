"""Tests for task04 - Sum0"""
from typing import List

import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    "a, b, c, d, res", [([1, 5], [-5, -1], [0, -8], [0, 2], 2), ([1], [2], [3], [4], 0)]
)
def test_result_as_num_of_sum_equal_null(
    a: List[int], b: List[int], c: List[int], d: List[int], res: int
):
    """Testing that the function returns
    the right number of cases where sum(i + j + k + m) = 0
    zero if there's not sum(i + j + k + m) = 0"""
    assert check_sum_of_four(a, b, c, d) == res
