# -*- coding: utf-8 -*-
"""
509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。



示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.


提示：

0 ≤ N ≤ 30
"""
class Solution:
    def fib_1(self, N: int) -> int:
        """
        方法一、动态规划（自底向上）
        时间复杂度：O(N)
        空间复杂度：O(1)
        :param N:
        :return:
        """
        a = 1
        b = 0
        for _ in range(N):
            c = a + b
            a, b = b, c
        return b

    def fib_2(self, N):
        """
        方法二、递归法（记忆化）
        时间复杂度：O(N)，每个fib(i)只计算一次，所以是O(N)
        空间复杂度：O(N)，递归系统栈开销O(N)
        :type N: int
        :rtype: int
        """
        cache = {}

        def recur_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N - 1) + recur_fib(N - 2)

            # put result in cache for later reference.
            cache[N] = result
            return result

        return recur_fib(N)


if __name__ == '__main__':
    n = 4
    solution = Solution()
    print(solution.fib_1(n))
    print(solution.fib_2(n))