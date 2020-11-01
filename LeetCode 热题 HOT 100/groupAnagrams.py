# -*- coding: utf-8 -*-
"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""
import collections
from typing import List


class Solution:
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        """
        时间复杂度：OO(NKlogK)
        空间复杂度：O(NK)
        :param strs:
        :return:
        """
        ans = collections.defaultdict(list)
        # print(list(ans.values()))
        for s in strs:
            # if not ans.get(tuple(sorted(s))):
            #     ans[tuple(sorted(s))] = [s]
            # else:
            ans[tuple(sorted(s))].append(s)

        # print(ans)

        return list(ans.values())

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    solution = Solution()
    print(solution.groupAnagrams_2(strs))
