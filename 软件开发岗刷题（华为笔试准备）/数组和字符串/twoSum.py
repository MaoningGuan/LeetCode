# -*- coding: utf-8 -*-
"""
167. 两数之和 II - 输入有序数组
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        双指针
        时间复杂度：O(n)，其中 n 是数组的长度。两个指针移动的总次数最多为 n 次。
        空间复杂度：O(1)。
        :param numbers:
        :param target:
        :return:
        """
        if not numbers:
            return []

        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    print(solution.twoSum(numbers, target))
