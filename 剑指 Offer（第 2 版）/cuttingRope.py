# -*- coding: utf-8 -*-
"""
剑指 Offer 14- I. 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
"""
class Solution:
    def cuttingRope(self, n: int) -> int:
        """
        方法三：动态规划（自底向上）
        时间复杂度：O(N^2)
        空间复杂度：O(N)
        :param n:
        :return:
        """
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.cuttingRope(10))
