# -*- coding: utf-8 -*-
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        """
        方法一：横向扫描
        时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。
        最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
        空间复杂度：O(1)。使用的额外空间复杂度为常数。
        :param strs:
        :return:
        """
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        """
        方法二：纵向扫描
        时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。
        最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。
        空间复杂度：O(1)。使用的额外空间复杂度为常数。
        :param strs:
        :return:
        """
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]

    def longestCommonPrefix_3(self, strs: List[str]) -> str:
        """
        方法四：二分查找
        时间复杂度：O(mnlogm)，其中 m 是字符串数组中的字符串的最小长度，n 是字符串的数量。
        二分查找的迭代执行次数是 O(logm)，每次迭代最多需要比较 mn 个字符，因此总时间复杂度是 O(mnlogm)。
        空间复杂度：O(1)O(1)。使用的额外空间复杂度为常数。
        :param strs:
        :return:
        """
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]

    solution = Solution()
    print(solution.longestCommonPrefix_3(strs))
