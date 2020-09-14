# -*- coding: utf-8 -*-
"""
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict={}
        for i in range(len(s)):
            if s[i] in dict:    #判断该元素是否之前出现过
                if dict[s[i]]!=t[i]:    #如果之前出现过，现在对应的值却不一样，返回False
                    return False
            else:
                if t[i] in dict.values():   #判断该元素是否在字典的值里面，如果在里面就说明对应的值不一样
                    return False
                dict[s[i]]=t[i] #将两个值录入字典中(记录下s[i]所变换后的字母)
        return True


if __name__ == '__main__':
    s = "paper"
    t = "title"

    solution = Solution()
    print(solution.isIsomorphic(s, t))


