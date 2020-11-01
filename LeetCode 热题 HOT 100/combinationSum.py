# -*- coding: utf-8 -*-
"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。
说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。
        方法：使用递归来实现回溯法
        :param candidates:
        :param target:
        :return:
        """
        ans = []
        temp = []

        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx])  # 选择使用第 idx 个数
            temp.pop()
            recursion(idx + 1, res)  # 选择跳过不用第 idx 个数

        recursion(0, 0)
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8

    solution = Solution()
    print(solution.combinationSum(candidates, target))
