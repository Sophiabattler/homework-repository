"""Task04 - Doctests"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function:
    takes a number N
    gives a list of N numbers as strings from 1 to N,
    where numbers multiples of 3 replace by "fizz"
    numbers multiples of 5 by "buzz"
    numbers multiples of 3 and 5 by "fizzbuzz"

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    >>> fizzbuzz(0)
    []
    """
    fizzbuzz_list = []
    if n < 1:
        return fizzbuzz_list
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizzbuzz_list.append("fizzbuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(str(i))
    return fizzbuzz_list
