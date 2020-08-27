# -*- coding: utf-8 -*-
"""
剑指 Offer 50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""


class Solution:
    def firstUniqChar_1(self, s: str) -> str:
        """
        方法一：哈希表
        时间复杂度 O(N) ： N 为字符串 s 的长度；需遍历 s 两轮，使用 O(N) ；HashMap 查找的操作复杂度为 O(1) ；
        空间复杂度 O(N) ： HashMap 需存储 N 个字符的键值对，使用 O(N) 大小的额外空间。
        :param s:
        :return:
        """
        dic = {}
        for c in s:
            dic[c] = not c in dic

        for c in s:
            if dic[c]:
                return c

        return " "

    def firstUniqChar_2(self, s: str) -> str:
        """
        方法二：有序哈希表
        基本原理：python 3.6后的字典是按照插入顺序来排序的，基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 11 的字符”。
        哈希表（字典）是 去重 的，即哈希表中键值对数量 ≤ 字符串 s 的长度。因此，相比于方法一，
        方法二减少了第二轮遍历的循环次数。当字符串很长（重复字符很多）时，方法二则效率更高。

        时间和空间复杂度均与 “方法一” 相同，而具体分析时间复杂度：
        方法一 O(2N) ： N 为字符串 s 的长度；需遍历 s 两轮；
        方法二 O(N) ：遍历 s 一轮，遍历 dic 一轮。
        :param s:
        :return:
        """
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '


if __name__ == '__main__':
    s = "leetcode"
    solution = Solution()
    print(solution.firstUniqChar_1(s))
    print(solution.firstUniqChar_2(s))
