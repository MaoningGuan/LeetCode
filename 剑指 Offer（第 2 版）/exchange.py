# -*- coding: utf-8 -*-
"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 
提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""
from typing import List
from collections import deque


class Solution:
    def exchange_1(self, nums: List[int]) -> List[int]:
        """
        双端队列
        时间复杂度 O(N)
        空间复杂度 O(N)
        :param nums:
        :return:
        """
        res = deque()
        for i in range(len(nums)):
            if nums[i] % 2 == 0:  # 偶数
                res.append(nums[i])
            else:
                res.appendleft(nums[i])
        return list(res)

    def exchange_2(self, nums: List[int]) -> List[int]:
        """
        双指针
        时间复杂度 O(N)
        空间复杂度 O(1)
        :param nums:
        :return:
        """
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.exchange_1(nums))
    print(solution.exchange_2(nums))
    print(nums)
