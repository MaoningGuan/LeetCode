# -*- coding: utf-8 -*-
"""
剑指 Offer 60. n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11

"""
from typing import List


class Solution:
    def twoSum_1(self, n: int) -> List[float]:
        """
        迭代
        :param n:
        :return:
        """
        if n == 0:
            return []
        # 初始化 1 - 6 是 1次，7 - n 是 0 次。
        # 编号从1开始，这样方便写代码。  为了从1开始，我们只需要在数组前面随便push一个元素即可，比如本例的0
        cnts = [0] + [1] * 6 + [0] * (6 * n - 6)
        # 模拟投掷 n - 1 次
        for _ in range(n - 1):
            # 从后向前更新
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])

        return list(filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, cnts))))

    def twoSum_2(self, n: int) -> List[float]:
        """
        递归
        :param n:
        :return:
        """
        def diceCnt(n):
            if n == 1:
                return [0] + [1] * 6
            cnts = diceCnt(n - 1) + [0] * 6
            for i in range(6 * n, 0, -1):
                cnts[i] = sum(cnts[max(i - 6, 0): i])
            return cnts

        return list(filter(lambda a: a != 0, list(map(lambda a: a / 6 ** n, diceCnt(n)))))


if __name__ == '__main__':
    n = 2
    solution = Solution()
    print(solution.twoSum_1(n))
    print(solution.twoSum_2(n))

