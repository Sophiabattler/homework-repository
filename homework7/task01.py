"""Task01 - Tree finder"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Count occurrences of element(type: str, list, tuple, dict, set, int, bool) in the tree"""

    def counting(item: Any):
        """Counting depending on element type"""
        nonlocal counter
        if item == element and type(item) == type(element):
            counter += 1
        elif isinstance(item, (bool, int)):
            pass
        elif item != element and not (isinstance(item, (str, bool, int))):
            if isinstance(item, dict):
                search_item_in_dict(item)
            elif isinstance(item, (list, tuple, set)):
                for elem in item:
                    counting(elem)

    def search_item_in_dict(same_tree: dict):
        """Looks for an element in the dictionary"""
        nonlocal counter
        if same_tree == element:
            counter += 1
        for key in same_tree.keys():
            counting(key)
            continue
        for value in same_tree.values():
            counting(value)
            continue

    counter = 0
    search_item_in_dict(tree)
    return counter
