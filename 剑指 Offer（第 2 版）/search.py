# -*- coding: utf-8 -*-
"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找
        时间复杂度 O(logN)： 二分法为对数级别复杂度。
        空间复杂度 O(1)： 几个变量使用常数大小的额外空间。
        :param nums:
        :param target:
        :return:
        """
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    solution = Solution()
    print(solution.search(nums, target))
