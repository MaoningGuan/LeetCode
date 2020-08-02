# -*- coding: utf-8 -*-
"""
5. 最长回文子串:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome_dp(self, s: str) -> str:
        """
        动态规划算法：自底向上解法
        算法时间复杂度：O(n^2)
        算法空间复杂度：O(n^2)
        :param s:目标字符串
        :return:最长回文子串
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):  # 从第一个字符开始枚举
                j = i + l
                if j >= len(s):
                    break
                if l == 0:  # 单个字符的子串
                    dp[i][j] = True
                elif l == 1:  # 两个字符的子串
                    dp[i][j] = (s[i] == s[j])
                else:  # 三个以上字符的子串
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])  # 动态规划的状态转移方程
                if dp[i][j] and l + 1 > len(ans):  # 子串的长度为 l + 1
                    ans = s[i:j + 1]  # 要取s[i:j + 1]，因为Python切片不包括j + 1位置的元素
        return ans

    def longestPalindrome_expandAroundCenter(self, s: str) -> str:
        """
        中心扩展算法，
        算法时间复杂度：O(n^2)
        算法空间复杂度：O(1)
        :param s:
        :return:
        """
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(s, i, i)
            left2, right2 = expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]



if __name__ == '__main__':
    solution = Solution()
    str_test = 'babaddaba'
    print(solution.longestPalindrome_expandAroundCenter(str_test))
