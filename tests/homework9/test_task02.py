"""Test for task02 - Suppressor"""
import pytest

from homework9.task02 import MySuppressor, my_suppressor


def test_class_suppresses_passed_exception():
    with MySuppressor(IndexError):
        [][1]


def test_class_does_not_suppress_another_exception():
    with pytest.raises(TypeError):
        with MySuppressor(IndexError):
            1[1]


def test_generator_suppresses_passed_exception():
    with my_suppressor(IndexError):
        [][1]


def test_generator_does_not_suppress_another_exception():
    with pytest.raises(TypeError):
        with my_suppressor(IndexError):
            1[1]
