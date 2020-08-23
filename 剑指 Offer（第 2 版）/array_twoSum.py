# -*- coding: utf-8 -*-
"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 
限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表
        时间和空间复杂度均为 O(N)
        :param nums:
        :param target:
        :return:
        """
        hashset = set()
        for num in nums:
            if (target - num) in hashset:
                return [target - num, num]
            else:
                hashset.add(num)

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
        双指针
        时间复杂度 O(N) ： N 为数组 nums 的长度；双指针共同线性遍历整个数组。
        空间复杂度 O(1) ： 变量 i, j 使用常数大小的额外空间。
        :param nums:
        :param target:
        :return:
        """
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    print(solution.twoSum_1(nums, target))
    print(solution.twoSum_2(nums, target))
