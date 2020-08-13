# -*- coding: utf-8 -*-
"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        题解：数学解法，我秀我自己
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # 同时从左往右和从右往左计算有效面积
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[- 1 - i] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        # 积水面积 = S1 + S2 - 矩形面积 - 柱子面积
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res

    def trap_simplify(self, height: List[int]) -> int:
        """
        题解：42.Python3三种方法以及详细思路——方法3，上面的方法的简化版。
        :param height:
        :return:
        """
        lmax, rmax, res = 0, 0, 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[-1 - i])
            res += lmax + rmax - height[i]
        return res - lmax * len(height)


if __name__ == '__main__':
    solution = Solution()
    trap_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solution.trap(trap_list))
    print(solution.trap_simplify(trap_list))
