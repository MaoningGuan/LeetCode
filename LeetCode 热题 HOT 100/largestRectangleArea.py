# -*- coding: utf-8 -*-
"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例:

输入: [2,1,5,6,2,3]
输出: 10
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        方法一：单调栈
        时间复杂度：O(N)O(N)。
        空间复杂度：O(N)O(N)。
        :param heights:
        :return:
        """
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        # 因为不包括左右边界的柱子：(right[i] - left[i] - 1)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

    def largestRectangleArea_optimize(self, heights: List[int]) -> int:
        """
        方法二：单调栈 + 常数优化
        时间复杂度：O(N)O(N)。
        空间复杂度：O(N)O(N)。
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


if __name__ == '__main__':
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(heights))
    print(solution.largestRectangleArea_optimize(heights))
