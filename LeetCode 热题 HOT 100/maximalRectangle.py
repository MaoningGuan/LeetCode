# -*- coding: utf-8 -*-
"""
85. 最大矩形
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
from typing import List


class Solution:
    def maximalRectangle_dp(self, matrix: List[List[str]]) -> int:
        """
        方法二：动态规划 - 使用柱状图的优化暴力方法
        时间复杂度 : O(N^2M)
        空间复杂度 : O(NM)
        :param matrix:
        :return:
        """
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea

        # Get the maximum area in a histogram given its heights

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        方法三：使用柱状图 - 栈
        时间复杂度 : O(NM)。对每一行运行 力扣 84 需要 M (每行长度) 时间，运行了 N 次，共计 O(NM)。
        空间复杂度 : O(M)。我们声明了长度等于列数的数组，用于存储每一行的宽度
        :param matrix:
        :return:
        """

        def leetcode84(heights):
            """
            84. 柱状图中最大的矩形：
            方法二：单调栈 + 常数优化
            时间复杂度：O(N)。
            空间复杂度：O(N)。
            :param self:
            :param heights:
            :return:
            """
            n = len(heights)
            left, right = [0] * n, [n] * n

            mono_stack = list()
            for i in range(n):
                while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                    right[mono_stack[-1]] = i
                    mono_stack.pop()
                left[i] = mono_stack[-1] if mono_stack else -1
                mono_stack.append(i)

            ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
            return ans

        if not matrix:
            return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # update maxarea with the maximum area from this row's histogram
            maxarea = max(maxarea, leetcode84(dp))
        return maxarea


if __name__ == '__main__':
    solution = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    # print(solution.maximalRectangle_dp(matrix))
    print(solution.maximalRectangle(matrix))
