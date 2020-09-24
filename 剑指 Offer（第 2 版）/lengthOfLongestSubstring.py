# -*- coding: utf-8 -*-
"""
剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        """
        方法一：动态规划 + 哈希表
        哈希表统计： 遍历字符串 s 时，使用哈希表（记为 dic ）统计 各字符最后一次出现的索引位置 。
        左边界 i 获取方式： 遍历到 s[j] 时，可通过访问哈希表 dic[s[j]] 获取最近的相同字符的索引 i 。
        时间复杂度 O(N) ： 其中 N 为字符串长度，动态规划需遍历计算 dp 列表。
        空间复杂度 O(1) ： 字符的 ASCII 码范围为 0 ~ 127 ，哈希表 dic 最多使用 O(128)=O(1) 大小的额外空间。
        :param s:
        :return:
        """
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        """
        方法二： 动态规划 + 线性遍历
        左边界 i 获取方式： 遍历到 s[j] 时，初始化索引 i = j - 1 ，向左遍历搜索第一个满足 s[i] = s[j]的字符即可 。
        时间复杂度 O(N^2)： 其中 N 为字符串长度，动态规划需遍历计算 dp 列表，占用 O(N) ；
        每轮计算 dp[j] 时搜索 i 需要遍历 j 个字符，占用 O(N) 。
        空间复杂度 O(1)： 几个变量使用常数大小的额外空间。
        :param s:
        :return:
        """
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        """
        方法三：双指针 + 哈希表
        复杂度分析：
        时间复杂度 O(N) ： 其中 N 为字符串长度，动态规划需遍历计算 dp 列表。
        空间复杂度 O(1) ： 字符的 ASCII 码范围为 0 ~ 127 ，哈希表 dic 最多使用 O(128)=O(1) 大小的额外空间。
        :param s:
        :return:
        """
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res


if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring_1(s))
    print(solution.lengthOfLongestSubstring_2(s))
    print(solution.lengthOfLongestSubstring_3(s))
