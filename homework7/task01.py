"""Task01 - Tree finder"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Count occurrences of element(type: str, list, tuple, dict, set, int, bool) in the tree"""

    def counting(item: Any):
        """Counting depending on element type"""
        nonlocal counter
        if item == element and type(item) == type(element):
            counter += 1
        elif type(item) == (bool or int):
            pass
        elif type(item) != (str or bool or int) and item != element:
            if type(item) == dict:
                search_item_in_dict(item)
            elif type(item) != (str and bool and int):
                for elem in item:
                    counting(elem)

    def search_item_in_dict(same_tree: dict):
        """Looks for an element in the dictionary"""
        nonlocal counter
        for key, value in same_tree.items():
            if element == {key: value}:
                counter += 1
                continue
        for key in same_tree.keys():
            counting(key)
            continue
        for value in same_tree.values():
            counting(value)
            continue

    counter = 0
    search_item_in_dict(tree)
    return counter


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # 6
