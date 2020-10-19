# -*- coding: utf-8 -*-
"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses_1(self, s: str) -> int:
        """
        常规方法
        时间复杂度：O(NlogN)，排序的时间复杂度
        空间复杂度：O(N)
        :param s:
        :return:
        """
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort()
        # print(res)
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans

    def longestValidParentheses(self, s: str) -> int:
        """
        动态规划
        时间复杂度：O(N)
        空间复杂度：O(N)
        :param s:
        :return:
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res


if __name__ == '__main__':
    s = "(()"

    solution = Solution()
    print(solution.longestValidParentheses(s))
