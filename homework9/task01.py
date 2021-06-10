"""Task01 - Iterator-merger"""
from pathlib import Path
from typing import Iterator, List, Union


def elements_from_file(file: Union[Path, str]) -> list:
    """Returns list of elements from the txt-file"""
    elem_from_file = []
    with open(file) as fi:
        for line in fi.readlines():
            elem_from_file.append(int(line.strip()))
    return elem_from_file


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """Returns iterator with sorted elements from all given txt-files"""
    merged_lists = []
    for file in file_list:
        merged_lists += elements_from_file(file)
    return iter(sorted(merged_lists))
