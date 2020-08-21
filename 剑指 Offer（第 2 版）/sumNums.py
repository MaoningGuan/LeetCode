# -*- coding: utf-8 -*-
"""
剑指 Offer 64. 求1+2+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例 1：

输入: n = 3
输出: 6
示例 2：
输入: n = 9
输出: 45

限制：

1 <= n <= 10000
"""


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        """
        递归法 + 逻辑符短路（终止递归）
        时间复杂度 O(n) ： 计算 n + (n-1) + ... + 2 + 1 需要开启 n 个递归函数。
        空间复杂度 O(n) ： 递归深度达到 n ，系统使用 O(n) 大小的额外空间
        :param n:
        :return:
        """
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    n = 9
    solution = Solution()
    print(solution.sumNums(n))
