# -*- coding: utf-8 -*-
"""
剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

限制：
1 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def majorityElement_1(self, nums: List[int]) -> int:
        """
        哈希表统计法
        时间和空间复杂度均为 O(N)
        :param nums:
        :return:
        """
        if not nums:  # 数组为空
            return 0

        hashset = {}
        for num in nums:
            hashset[num] = hashset[num] + 1 if hashset.get(num) else 1
            # if hashset[num] > len(nums) / 2:   # Python3.6之后下面的字典迭代要比这里的列表迭代要快，所以验证众数使用下面的字典迭代
            #     return num

        for key, value in hashset.items():
            if value > len(nums) / 2:
                return key
        return 0  # 不存在众数

    def majorityElement_2(self, nums: List[int]) -> int:
        """
        组排序法
        时间复杂度 ： O(NlogN)，Python内置排序算法Timsort的时间复杂度
        空间复杂度 ：不需要用到额外的空间
        :param nums:
        :return:
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_3(self, nums: List[int]) -> int:
        """
        摩尔投票法
        时间和空间复杂度分别为 O(N) 和 O(1)
        :param nums:
        :return:
        """
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]

    solution = Solution()
    print(solution.majorityElement_1(nums))
    print(solution.majorityElement_2(nums))
    print(solution.majorityElement_3(nums))
