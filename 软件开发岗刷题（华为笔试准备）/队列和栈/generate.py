# -*- coding: utf-8 -*-
"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List


class Solution:
    def generate_1(self, numRows: int) -> List[List[int]]:
        """
        递归
        时间复杂度：O(numRows^3)
        空间复杂度：O(numRows^2)
        :param numRows:
        :return:
        """

        def recur(i, j):
            if j == 0 or i == j:
                return 1
            else:
                return recur(i - 1, j - 1) + recur(i - 1, j)

        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or i == j:
                    tmp.append(1)
                else:
                    tmp.append(recur(i - 1, j - 1) + recur(i - 1, j))
            res.append(tmp)

        return res

    def generate_2(self, numRows: int) -> List[List[int]]:
        """
        动态规划
        时间复杂度：O(numRows^2)
        空间复杂度：O(numRows^2)
        :param numRows:
        :return:
        """
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or i == j:
                    tmp.append(1)
                else:
                    tmp.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(tmp)

        return res


if __name__ == '__main__':
    n = 5
    solution = Solution()
    print(solution.generate_2(n))
