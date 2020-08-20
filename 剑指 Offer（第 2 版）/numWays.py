# -*- coding: utf-8 -*-
"""
剑指 Offer 10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100
"""
class Solution:
    def numWays(self, n: int) -> int:
        """
        动态规划
        时间复杂度 O(N)： 计算 f(n) 需循环 n 次，每轮循环内计算操作使用 O(1) 。
        空间复杂度 O(1)： 几个标志变量使用常数大小的额外空间。
        :param n:
        :return:
        """
        ways_1 = 0
        ways_2 = 1
        if n == 0:
            return ways_2
        if n < 0:
            return -1
        for _ in range(n):
            ways = ways_1 + ways_2
            ways_1 = ways_2
            ways_2 = ways
        return ways % 1000000007


if __name__ == '__main__':
    n = 7
    solution = Solution()
    print(solution.numWays(n))

