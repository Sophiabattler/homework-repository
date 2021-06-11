"""Test for task01 - Tree finder"""
from homework7.task01 import find_occurrences


def test_different_types_of_required_element():
    tree = {True: {1: (1, 1)}, 2: (["nested", 1], {1: (1, 1)}, "nested", ["nested", 3])}
    assert find_occurrences(tree, tree) == 1
    assert find_occurrences(tree, True) == 1
    assert find_occurrences(tree, 1) == 7
    assert find_occurrences(tree, (1, 1)) == 2
    assert find_occurrences(tree, {1: (1, 1)}) == 2
    assert find_occurrences(tree, ["nested", 1]) == 1
    assert find_occurrences(tree, "nested") == 3


def test_if_there_is_not_required_element_in_a_tree():
    tree = {True: 1}
    assert find_occurrences(tree, 2) == 0
