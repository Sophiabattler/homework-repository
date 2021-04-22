"""Tests for task02_var1 - Fibonacci"""
from typing import Sequence

import pytest

from homework1.task02_var1 import check_fibonacci


@pytest.mark.parametrize(
    "val",
    [[0, 1, 1], [0, 1, 1, 2, 3, 5, 8], [0, 1, 1, 2]],
)
def test_positive_amount_of_elem(val: Sequence[int]):
    """Testing that:
    sequence starts like the Fibonacci sequence
    sequence contains enough elements
    all the sequence is the Fibonacci sequence"""
    assert check_fibonacci(val) is True


@pytest.mark.parametrize(
    "val",
    [[1, 1, 2, 3, 5, 8], [0], [0, 1, 1, 2, 3, 5, 8, 12]],
)
def test_negative_start_fibonacci(val: Sequence[int]):
    """Testing that:
    sequence doesn't start like the Fibonacci sequence
    sequence doesn't contain enough elements
    all the sequence isn't the Fibonacci sequence"""
    assert check_fibonacci(val) is False
