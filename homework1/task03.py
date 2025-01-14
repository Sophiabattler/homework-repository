"""Task03 - Min&max"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find minimum and maximum and return them as a tuple"""
    with open(file_name) as fi:
        mini = int(fi.readline())
        maxi = mini
        for line in fi:
            line_int = int(line)
            maxi = max(maxi, line_int)
            mini = min(mini, line_int)
        return mini, maxi
