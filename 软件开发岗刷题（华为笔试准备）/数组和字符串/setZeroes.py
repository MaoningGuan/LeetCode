# -*- coding: utf-8 -*-
"""
面试题 01.08. 零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。



示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        时间复杂度：O(MN)
        空间复杂度：O(M + N)
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in column:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        return


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)
