# -*- coding: utf-8 -*-
"""
寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 数组只有一个元素
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        # 数组没有反转
        if nums[r] > nums[0]:
            return nums[0]

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]

    solution = Solution()
    print(solution.findMin(nums))
