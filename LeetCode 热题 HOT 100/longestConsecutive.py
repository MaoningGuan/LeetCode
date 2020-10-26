# -*- coding: utf-8 -*-
"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。



进阶：

你可以设计并实现时间复杂度为 O(n) 的解决方案吗？


示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)

        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                current_num = num

                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]

    solution = Solution()
    print(solution.longestConsecutive(nums))
