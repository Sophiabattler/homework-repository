"""Test for task01 - Iterator-merger"""
from homework9.task01 import merge_sorted_files


def test_merge_sorted_files_merge_numbers_in_right_order(tmp_path):
    path_to_first_file = tmp_path / "file1.txt"
    with open(path_to_first_file, "w") as fi:
        fi.write("11\n8\n")
    path_to_second_file = tmp_path / "file2.txt"
    with open(path_to_second_file, "w") as fi:
        fi.write("1\n2\n6\n")
    iterator = merge_sorted_files([path_to_first_file, path_to_second_file])
    assert list(iterator) == [1, 2, 6, 8, 11]
