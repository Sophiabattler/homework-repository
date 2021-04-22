"""Tests for task05 - Find a sub-array"""
from typing import List

import pytest

from homework1.task05 import find_maximal_sub_array_sum


@pytest.mark.parametrize(
    "nums, k, res", [([], 1, 0), ([1, 2, 3], 10, 6), ([-5, -1, 1], 2, 1)]
)
def test_return_max_sub_array(nums: List, k: int, res: int):
    """Testing that the function returns
    0, if nums is empty
    full list, if k>len(nums)
    the right max_sum"""
    assert find_maximal_sub_array_sum(nums, k) == res
