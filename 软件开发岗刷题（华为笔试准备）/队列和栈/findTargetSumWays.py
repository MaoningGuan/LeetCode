# -*- coding: utf-8 -*-
"""
494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。



示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。


提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        dfs深度优先搜索
        时间复杂度：O(2^N)，N为nums的元素个数
        空间复杂度：O(N)，N为nums的元素个数，递归深度为N
        :param nums:
        :param S:
        :return:
        """
        d = {}

        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d:  # 搜索周围节点
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)
            return d.get((cur, i), int(cur == S))

        return dfs(0, 0, d)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3

    solution = Solution()
    print(solution.findTargetSumWays(nums, S))
