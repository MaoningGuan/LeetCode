# -*- coding: utf-8 -*-
"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]


说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
import collections
from typing import List


class Solution:
    def intersect_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法一：哈希表
        时间复杂度：O(m+n)，其中 m 和 n 分别是两个数组的长度。需要遍历两个数组并对哈希表进行操作，
        哈希表操作的时间复杂度是 O(1)，因此总时间复杂度与两个数组的长度和呈线性关系。
        空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个数组的长度。对较短的数组进行哈希表的操作，
        哈希表的大小不会超过较短的数组的长度。为返回值创建一个数组 intersection，其长度为较短的数组的长度。
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) > len(nums2):
            return self.intersect_1(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if m.get(num, 0) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        时间复杂度：(mlogm+nlogn)，对两个数组排序的时间
        空间复杂度：O(min(m,n))，其中 m 和 n 分别是两个数组的长度。为返回值创建一个数组 intersection，其长度为较短的数组的长度。
        :param nums1:
        :param nums2:
        :return:
        """
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1

        return intersection


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    solution = Solution()
    print(solution.intersect_1(nums1, nums2))
    print(solution.intersect_2(nums1, nums2))
