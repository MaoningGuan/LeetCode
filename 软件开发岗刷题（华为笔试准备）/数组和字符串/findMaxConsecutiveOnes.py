# -*- coding: utf-8 -*-
"""
485. 最大连续1的个数
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes_1(self, nums: List[int]) -> int:
        """
        时间复杂度：O(N)。N 值得是数组的长度。
        空间复杂度：O(1)，仅仅使用了 count 和 maxCount。
        :param nums:
        :return:
        """
        count = max_count = 0
        for num in nums:
            if num == 1:
                # Increment the count of 1's by one.
                count += 1
            else:
                # Find the maximum till now.
                max_count = max(max_count, count)
                # Reset count of 1.
                count = 0
        return max(max_count, count)  # 防止最后几个元素全为1，而没有进入else来更新max_count

    def findMaxConsecutiveOnes_2(self, nums):
        """
        时间复杂度：O(N)。N 值得是数组的长度。
        空间复杂度：O(N)。
        :param nums:
        :return:
        """
        return max(map(len, ''.join(map(str, nums)).split('0')))


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]

    solution = Solution()
    print(solution.findMaxConsecutiveOnes_1(nums))
    print(solution.findMaxConsecutiveOnes_2(nums))
