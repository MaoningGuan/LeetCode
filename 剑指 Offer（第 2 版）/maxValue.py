# -*- coding: utf-8 -*-
"""
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 
提示：

0 < grid.length <= 200
0 < grid[0].length <= 200
"""
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                dp[row][column] = max(dp[row - 1][column], dp[row][column - 1]) + grid[row - 1][column - 1]
        return dp[rows][columns]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    solution = Solution()
    print(solution.maxValue(grid))
