# -*- coding: utf-8 -*-
"""
179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        """
        自定义排序：
        时间复杂度：O(nlgn)。尽管我们在比较函数中做了一些额外的工作，但是这只是一个常数因子。
        所以总的时间复杂度是由排序决定的，在 Python 和 Java 中都是 O(nlgn) 。
        空间复杂度：空间复杂度：O(n)
        这里，我们使用了 O(n) 的额外空间去保存 nums 的副本。尽管我们就地进行了一些额外的工作，
        但最后返回的数组需要 O(n) 的空间。因此，需要的额外空间与 nums 大小成线性关系。
        :param nums:
        :return:
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]

    solution = Solution()
    print(solution.largestNumber(nums))
