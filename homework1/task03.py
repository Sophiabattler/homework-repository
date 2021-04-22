"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Giving the min and max values of integers in read file."""
    minimum, maximum = float("inf"), float("-inf")
    with open(file_name) as fi:
        for line in fi:
            number = int(line.strip())
            minimum = number if number < minimum else minimum
            maximum = number if number > maximum else maximum
    return minimum, maximum
