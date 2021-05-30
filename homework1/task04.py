"""Task04 - Sum0"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Compute how many tuples (i, j, k, m) there are such
    that A[i] + B[j] + C[k] + D[m] is zero"""
    sums = {}
    for i in a:
        for j in b:
            if i + j not in sums:
                sums[i + j] = 1
            else:
                sums[i + j] += 1
    counter = 0
    for k in c:
        for m in d:
            if -1 * (k + m) in sums:
                counter += sums[-1 * (k + m)]
    return counter
