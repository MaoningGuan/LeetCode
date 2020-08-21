# -*- coding: utf-8 -*-
"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划
        时间复杂度 O(N) ： 其中 N 为 prices 列表长度，动态规划需遍历 prices 。
        空间复杂度 O(1) ： 变量 cost 和 profit 使用常数大小的额外空间。。
        :param prices:
        :return:
        """
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices))
