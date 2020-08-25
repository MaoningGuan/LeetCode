# -*- coding: utf-8 -*-
"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

限制：

0 <= n <= 1000

0 <= m <= 1000
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    solution = Solution()
    print(solution.findNumberIn2DArray(matrix, 5))
    print(solution.findNumberIn2DArray(matrix, 20))
