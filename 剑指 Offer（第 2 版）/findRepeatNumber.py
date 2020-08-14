# -*- coding: utf-8 -*-
"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
 
限制：

2 <= n <= 100000
"""
from typing import List


class Solution:
    def findRepeatNumber_1(self, nums: List[int]) -> int:
        """
        方法一：哈希表 / Set
        时间复杂度 O(N) ： 遍历数组使用 O(N) ，HashSet 添加与查找元素皆为 O(1) 。
        空间复杂度 O(N) ： HashSet 占用 O(N) 大小的额外空间。
        :param nums:
        :return:
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return num
            else:
                hashset.add(num)
        return -1
        # hashset = {}
        # for num in nums:
        #     if hashset.get(num) is not None:
        #         return num
        #     else:
        #         hashset[num] = num

    def findRepeatNumber_2(self, nums: [int]) -> int:
        """
        方法二：原地交换
        时间复杂度 O(N) ： 遍历数组使用 O(N) ，每轮遍历的判断和交换操作使用 O(1) 。
        空间复杂度 O(1) ： 使用常数复杂度的额外空间。
        :param nums:
        :return:
        """
        nums = nums.copy()
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 4, 1, 0, 2, 5, 3]
    print(solution.findRepeatNumber_1(nums))
    print(solution.findRepeatNumber_2(nums))





