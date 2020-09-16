# -*- coding: utf-8 -*-
"""
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。


示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。


进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
import bisect
from typing import List


class Solution:
    def minSubArrayLen_1(self, s: int, nums: List[int]) -> int:
        def binarySearch(sums, target):
            l = 0
            r = len(sums) - 1

            while l < r:
                mid = (l + r) // 2

                if sums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l if sums[l] >= target else l + 1

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = binarySearch(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans

    def minSubArrayLen_2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]

    solution = Solution()
    print(solution.minSubArrayLen_1(s, nums))
    print(solution.minSubArrayLen_2(s, nums))
