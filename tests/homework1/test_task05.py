"""Tests for task05 - Find a sub-array"""

from homework1.task05 import find_maximal_sub_array_sum


def test_if_empty_list_return_null():
    """Testing that the function returns 0, if nums is empty"""
    assert find_maximal_sub_array_sum([], 1) == 0


def test_k_more_then_length_sums_return_full_list():
    """Testing that the function returns full list, if k>len(nums)"""
    assert find_maximal_sub_array_sum([1, 2, 3], 10) == 6


def test_with_positive_and_negative_numbers():
    """Testing that the function returns the right max_sum,
    where might be positive and negative numbers"""
    assert find_maximal_sub_array_sum([-5, -1, 1], 2) == 1
