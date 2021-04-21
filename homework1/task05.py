"""Task05 - Find a sub-array"""

from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    """Finding a sub-array with length less equal
    to "k", with maximal sum"""
    cur_num_elem = 0
    start_from_elem = 0
    current_sum = float("-inf")
    max_sum = float("-inf")
    i = 0
    if len(nums) == 0:
        return 0
    while start_from_elem < len(nums):
        while i < k:
            if cur_num_elem < len(nums):
                if current_sum <= 0 and i == 0:
                    current_sum = nums[cur_num_elem]
                else:
                    current_sum += nums[cur_num_elem]
            i += 1
            cur_num_elem += 1

            if current_sum > max_sum:
                max_sum = current_sum
        start_from_elem += 1
        cur_num_elem = cur_num_elem - k + 1
        i = 0
        current_sum = 0

    return max_sum
