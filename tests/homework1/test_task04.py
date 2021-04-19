"""Tests for task04 - Sum0"""

from homework1.task04 import check_sum_of_four


def test_positive_result():
    """Testing that the function returns the right number
    of cases where sum(i + j + k + m) = 0"""
    assert check_sum_of_four([1, 5], [-5, -1], [0, -8], [0, 2]) == 2


def test_zero_result():
    """Testing that the function will return zero
    if there's not sum(i + j + k + m) = 0"""
    assert check_sum_of_four([1, 5], [-20, -110], [0, -8], [11000, 14]) == 0
