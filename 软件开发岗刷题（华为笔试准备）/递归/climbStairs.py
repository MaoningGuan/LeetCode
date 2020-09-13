# -*- coding: utf-8 -*-
"""
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        方法一、递归法（记忆化）
        时间复杂度：O(N)。计算每一个recur(i)，i = 1,2,3,...,n，所以是O(N)
        空间复杂度：O(N)。存储每一个recur(i)，i = 1,2,3,...,n，所以是O(N)
        :param n:
        :return:
        """
        cache = {1: 1, 2: 2}

        def recur(n: int) -> int:
            if n in cache:
                result = cache[n]
            else:
                result = recur(n - 1) + recur(n - 2)
                cache[n] = result

            return result

        if n in cache:
            return cache[n]
        else:
            return recur(n - 1) + recur(n - 2)


    def climbStairs_2(self, n: int) -> int:
        """
        方法二、动态规划（自底向上）
        时间复杂度：O(N)。计算每一个climbStairs(i)，i = 1,2,3,...,n，所以是O(N)
        空间复杂度：O(1)。
        :param n:
        :return:
        """
        a = 0
        b = 1
        for _ in range(n):
            c = a + b
            a, b = b, c
        return b


if __name__ == '__main__':
    n = 4

    solution = Solution()
    print(solution.climbStairs_2(n))
