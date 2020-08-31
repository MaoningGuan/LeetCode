# -*- coding: utf-8 -*-
"""
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return

        hashset = {}
        for num in nums:
            if hashset.get(num):
                hashset[num] += 1
            else:
                hashset[num] = 1

        for key, value in hashset.items():
            if value == 1:
                return key


if __name__ == '__main__':
    nums = [9, 1, 7, 9, 7, 9, 7]

    solution = Solution()
    print(solution.singleNumber(nums))
