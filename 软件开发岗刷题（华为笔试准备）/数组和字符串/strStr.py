# -*- coding: utf-8 -*-
"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""
class Solution:
    def strStr_1(self, haystack: str, needle: str) -> int:
        """
        方法一：子串逐一比较 - 线性时间复杂度
        时间复杂度：O((N−L)L)，其中 N 为 haystack 字符串的长度，L 为 needle 字符串的长度。
        内循环中比较字符串的复杂度为 L，总共需要比较 (N - L) 次。
        空间复杂度：O(1)。
        :param haystack:
        :param needle:
        :return:
        """
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

    def strStr_2(self, haystack: str, needle: str) -> int:
        """
        方法二：双指针 - 线性时间复杂度
        时间复杂度：最坏时间复杂度为 O((N - L)L)，最优时间复杂度为 O(N)。
        空间复杂度：O(1)。
        :param haystack:
        :param needle:
        :return:
        """
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            # find the position of the first needle character
            # in the haystack string
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            # compute the max match string
            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1

            # if the whole needle string is found,
            # return its start position
            if curr_len == L:
                return pn - L

            # otherwise, backtrack
            pn = pn - curr_len + 1

        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"

    solution = Solution()
    print(solution.strStr_1(haystack, needle))
    print(solution.strStr_2(haystack, needle))
