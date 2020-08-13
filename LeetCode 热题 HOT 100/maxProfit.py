# -*- coding: utf-8 -*-
"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""
from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        """
        方法一：动态规划
        时间复杂度：O(n)，其中 n 为数组 prices 的长度。
        空间复杂度：O(n)。我们需要 3n 的空间存储动态规划中的所有状态，对应的空间复杂度为 O(n)。
        :param prices:
        :return:
        """
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])

    def maxProfit_2(self, prices: List[int]) -> int:
        """
        方法一：动态规划（空间优化）
        时间复杂度：O(n)，其中 n 为数组 prices 的长度。
        空间复杂度：O(1)。使用空间优化，空间复杂度可以优化至 O(1)。
        :param prices:
        :return:
        """
        if not prices:
            return 0

        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            newf0 = max(f0, f2 - prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1, f2)
            f0, f1, f2 = newf0, newf1, newf2

        return max(f1, f2)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    solution = Solution()
    print(solution.maxProfit_1(prices))
    print(solution.maxProfit_2(prices))

