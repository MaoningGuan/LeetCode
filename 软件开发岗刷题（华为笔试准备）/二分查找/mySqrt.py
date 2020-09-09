# -*- coding: utf-8 -*-
"""
x的平方根
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

由于 x 平方根的整数部分 ans 是满足 k^2 ≤ x 的最大 k 值，因此我们可以对 k 进行二分查找，从而得到答案。
二分查找的下界为 0，上界可以粗略地设定为 x。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分查找
        时间复杂度：O(logx)，即为二分查找需要的次数。
        空间复杂度：O(1)。
        :param x:
        :return:
        """
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    x = 8
    solution = Solution()
    print(solution.mySqrt(x))
