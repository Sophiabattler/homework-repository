""""Test for task01 - KeyValueStorage"""
import pytest

from homework8.task01 import KeyValueStorage

text_of_txt_file = "name=kek\npower=9001"


def test_value_error_in_case_of_incorrect_key(tmp_path):
    path_to_file_with_error = tmp_path / "error.txt"
    incorrect_key = "error key = some"
    with open(path_to_file_with_error, "w") as fi:
        fi.write(incorrect_key)
    with pytest.raises(ValueError):
        KeyValueStorage(path_to_file_with_error)


def test_access_to_keys_in_different_ways_with_values_as_str_and_as_int(tmp_path):
    path_to_file = tmp_path / "task.txt"
    with open(path_to_file, "w") as fi:
        fi.write(text_of_txt_file)
    storage = KeyValueStorage(path_to_file)
    assert storage["name"] == "kek"
    assert storage.name == "kek"
    assert isinstance(storage.name, str)
    assert storage.power == 9001
    assert isinstance(storage.power, int)


def test_no_such_element_in_the_file(tmp_path):
    path_to_file = tmp_path / "task.txt"
    with open(path_to_file, "w") as fi:
        fi.write(text_of_txt_file)
    storage = KeyValueStorage(path_to_file)
    with pytest.raises(AttributeError):
        storage.not_key
    with pytest.raises(KeyError):
        storage["not_key"]


def test_precedence_of_built_in_attributes(tmp_path):
    path_to_file = tmp_path / "text.txt"
    built_it_key = "__class__=123"
    with open(path_to_file, "w") as fi:
        fi.write(built_it_key)
    storage = KeyValueStorage(path_to_file)
    assert storage["__class__"] == 123
    assert not storage["__class__"] == storage.__class__
    assert isinstance(storage.__class__, type)
