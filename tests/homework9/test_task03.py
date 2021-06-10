"""Test for task03 - Count lines or tokens"""
from homework9.task03 import universal_file_counter


def test_case_without_tokenizer_returns_amount_of_lines(tmp_path):
    path_to_first_file = tmp_path / "file1.txt"
    path_to_second_file = tmp_path / "file2.txt"
    with open(path_to_first_file, "w") as fi:
        fi.write("a b c\n")
    with open(path_to_second_file, "w") as fi:
        fi.write("d e\nf\n")
    assert universal_file_counter(tmp_path, "txt") == 3


def test_case_with_tokenizer_split_returns_amount_of_tokens(tmp_path):
    path_to_first_file = tmp_path / "file1.txt"
    path_to_second_file = tmp_path / "file2.txt"
    with open(path_to_first_file, "w") as fi:
        fi.write("a b c\n")
    with open(path_to_second_file, "w") as fi:
        fi.write("d e\nf g\n")
    assert universal_file_counter(tmp_path, "txt", str.split) == 7
