# -*- coding: utf-8 -*-
"""
剑指 Offer 62. 圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2

限制：

1 <= n <= 10^5
1 <= m <= 10^6
"""
import sys


# Python 默认的递归深度不够，需要手动设置
sys.setrecursionlimit(100000)


class Solution:
    def lastRemaining_1(self, n: int, m: int) -> int:
        """
        参考LeetCode官方的题解
        方法一：数学 + 递归
        时间复杂度：O(n)，需要求解的函数值有 n 个。
        空间复杂度：O(n)，函数的递归深度为 n，需要使用 O(n) 的栈空间。
        :param n:
        :param m:
        :return:
        """
        def f(n, m):
            if n == 0:
                return 0
            x = f(n - 1, m)
            return (m + x) % n

        return f(n, m)

    def lastRemaining_2(self, n: int, m: int) -> int:
        """
        参考LeetCode官方的题解
        方法二：数学 + 迭代
        时间复杂度：O(n)，需要求解的函数值有 nn 个。
        空间复杂度：O(1)，只使用常数个变量。
        :param n:
        :param m:
        :return:
        """
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == '__main__':
    n = 10
    m = 17

    solution = Solution()
    print(solution.lastRemaining_1(n, m))
    print(solution.lastRemaining_2(n, m))

