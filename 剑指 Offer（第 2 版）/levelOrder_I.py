# -*- coding: utf-8 -*-
"""
剑指 Offer 32 - I. 从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 
提示：
节点总数 <= 1000
"""
import collections
from typing import List

from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        """
        层序遍历 BFS
        时间复杂度 O(N)： N 为二叉树的节点数量，即 BFS 需循环 N 次。
        空间复杂度 O(N)： 最差情况下，即当树为平衡二叉树时，最多有 N/2 个树节点同时在 queue 中，使用 O(N) 大小的额外空间。
        :param root:
        :return:
        """
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res


if __name__ == '__main__':
    root = deserialize("[3,9,20,null,null,15,7]")

    solution = Solution()
    print(solution.levelOrder(root))
