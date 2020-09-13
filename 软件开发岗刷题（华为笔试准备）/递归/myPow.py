# -*- coding: utf-8 -*-
"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


class Solution:
    def myPow_1(self, x: float, n: int) -> float:
        """
        方法一：快速幂 + 递归
        时间复杂度：O(logn)，即为递归的层数。
        空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。
        :param x:
        :param n:
        :return:
        """

        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow_2(self, x: float, n: int) -> float:
        """
        方法二：快速幂 + 迭代
        时间复杂度：O(logn)，即为对 nn 进行二进制拆分的时间复杂度。
        空间复杂度：O(1)。
        :param x:
        :param n:
        :return:
        """

        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    x = 2.0
    n = 10

    solution = Solution()
    print(solution.myPow_1(x, n))
    print(solution.myPow_2(x, n))
