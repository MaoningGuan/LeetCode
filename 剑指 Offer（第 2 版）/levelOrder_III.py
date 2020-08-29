# -*- coding: utf-8 -*-
"""
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000
"""
from collections import deque
from typing import List

from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            tmp = deque()
            nodes = []
            for node in queue:
                if len(res) & 1:  # 偶数层
                    tmp.appendleft(node.val)
                else:  # 奇数层
                    tmp.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(list(tmp))
            queue = nodes

        return res


if __name__ == '__main__':
    tree_str = "[3,9,20,null,null,15,7]"
    root = deserialize(tree_str)

    solution = Solution()
    print(solution.levelOrder(root))
