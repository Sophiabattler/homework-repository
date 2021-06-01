"""Task05 - Find a sub-array"""
from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    """Finding a sub-array with length less equal
    to "k", with maximal sum"""
    max_sum = float("-inf")
    if len(nums) < k:
        k = len(nums)
    if len(nums) == 0:
        max_sum = 0
    for n in range(k + 1):
        for i in range(len(nums)):
            num_cut = nums[i : i + n]
            new_sum = sum(num_cut)
            max_sum = max(max_sum, new_sum)
    return max_sum
