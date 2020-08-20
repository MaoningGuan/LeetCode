# -*- coding: utf-8 -*-
"""
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        时间复杂度 O(N) ： 线性遍历数组 nums 即可获得结果，使用 O(N) 时间。
        空间复杂度 O(1) ： 使用常数大小的额外空间。
        :param nums:
        :return:
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    print(solution.maxSubArray(nums))
