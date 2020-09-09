# -*- coding: utf-8 -*-
"""
1. 两数之和：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""
from typing import List


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        暴力法
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
        排序 + 双指针
        :param nums:
        :param target:
        :return:
        """
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if (temp[i] + temp[j]) > target:
                j = j - 1
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            else:
                break
        if i == j:
            return []
        p = nums.index(temp[i])
        nums.pop(p)
        k = nums.index(temp[j])
        if k >= p:
            k = k + 1
        return [p, k]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hash解法，耗时最少
        时间复杂度：O(N)
        空间复杂度：O(N)
        :param nums:
        :param target:
        :return:
        """
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target - nums[i]) is not None:
                return [hashset.get(target - nums[i]), i]
            hashset[nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    index = solution.twoSum(nums, target)
    print(index)
