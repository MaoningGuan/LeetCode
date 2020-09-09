# -*- coding: utf-8 -*-
"""
二分查找模板1
"""
from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9

    nums = []
    target = 2

    solution = Solution()
    print(solution.binarySearch(nums, target))
