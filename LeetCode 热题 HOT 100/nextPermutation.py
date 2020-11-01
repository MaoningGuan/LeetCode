# -*- coding: utf-8 -*-
"""
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        方法：一遍扫描
        时间复杂度：O(n)，在最坏的情况下，只需要对整个数组进行两次扫描。
        空间复杂度：O(1)，没有使用额外的空间，原地替换足以做到。
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])

        return nums


if __name__ == '__main__':
    nums = [1,5,1]

    solution = Solution()
    print(solution.nextPermutation(nums))
