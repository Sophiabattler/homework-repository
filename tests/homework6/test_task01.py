"""Test for task01 - Count instances"""
import pytest

from homework6.task01 import instances_counter


@pytest.fixture
def decorated():
    class MyClass:
        pass

    return instances_counter(MyClass)


def test_first_call_reset_give_zero(decorated):
    assert decorated.get_created_instances() == 0


def test_counter_returns_right_number_of_instances(decorated):
    instance, _, _ = decorated(), decorated(), decorated()
    assert instance.get_created_instances() == 3


def test_counter_returns_last_counter_and_resets_instances_counter(decorated):
    instance, _, _ = decorated(), decorated(), decorated()
    assert instance.reset_instances_counter() == 3
    assert decorated.get_created_instances() == 0
