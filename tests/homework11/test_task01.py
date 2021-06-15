"""Test for task01 - Metaclass"""
from homework11.task01 import SimplifiedEnum


def test_metaclass_simplified_sets_colors_enum_attrs_in__keys():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE == "ORANGE"
