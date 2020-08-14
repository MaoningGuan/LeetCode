# -*- coding: utf-8 -*-
"""
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:

输入: [7,5,6,4]
输出: 5
 
限制：
0 <= 数组长度 <= 50000
"""
from typing import List


class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs_1(self, nums: List[int]) -> int:
        """
        方法一：归并排序
        记序列长度为 n。
        时间复杂度：同归并排序 O(nlogn)。
        空间复杂度：同归并排序 O(n)，因为归并排序需要用到一个临时数组。
        :param nums:
        :return:
        """
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


if __name__ == '__main__':
    nums = [7, 5, 6, 4]

    solution = Solution()
    print(solution.reversePairs_1(nums))

