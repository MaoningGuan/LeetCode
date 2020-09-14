# -*- coding: utf-8 -*-
"""
349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]


说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法二：内置函数
        时间复杂度：一般情况下是 O(m+n)，最坏情况下是 O(m×n) 。
        空间复杂度：最坏的情况是 O(m+n)，数组中的所有元素都不同。
        :param nums1:
        :param nums2:
        :return:
        """
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1 & s2)


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]

    solution = Solution()
    print(solution.intersection(nums1, nums2))
