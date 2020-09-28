# -*- coding: utf-8 -*-
"""
312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List


class Solution:
    def maxCoins_1(self, nums: List[int]) -> int:
        """
        方法一：记忆化搜索
        时间复杂度：O(n^3)，其中 n 是气球数量。区间数为 n^2，区间迭代复杂度为 O(n)，最终复杂度为 O(n^2 x n) = O(n^3)
        空间复杂度：O(n^2)，其中 n 是气球数量。缓存大小为区间的个数。
        :return:
        """
        n = len(nums)
        val = [1] + nums + [1]

        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0

            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)

            return best

        return solve(0, n + 1)

    def maxCoins_2(self, nums: List[int]) -> int:
        """
        方法二：动态规划
        时间复杂度：O(n^3)，其中 n 是气球数量。状态数为 n^2，状态转移复杂度为 O(n)，最终复杂度为 O(n^2 x n) = O(n^3)
        空间复杂度：O(n^2)，其中 n 是气球数量。缓存大小为区间的个数。
        :param nums:
        :return:
        """
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]




if __name__ == '__main__':
    nums = [3, 1, 5, 8]

    solution = Solution()
    print(solution.maxCoins(nums))
