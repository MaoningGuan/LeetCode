# -*- coding: utf-8 -*-
"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。



示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


提示：你可以假定该字符串只包含小写字母。
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap[s[i]] + 1 if s[i] in hashmap else 1

        # find the index
        for idx, ch in enumerate(s):
            if hashmap[ch] == 1:
                return idx
        return -1



if __name__ == '__main__':
    s = "loveleetcode"

    solution = Solution()
    print(solution.firstUniqChar(s))


