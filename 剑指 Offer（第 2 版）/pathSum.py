# -*- coding: utf-8 -*-
"""
剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

提示：
节点总数 <= 10000
"""
from typing import List
from utils import deserialize, printTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        回溯法
        深度优先搜索
        时间复杂度 O(N)O(N) ： N 为二叉树的节点数，先序遍历需要遍历所有节点。
        空间复杂度 O(N)O(N) ： 最差情况下，即树退化为链表时，path 存储所有树节点，使用 O(N) 额外空间。
        :param root:
        :param sum:
        :return:
        """
        res, path = [], []

        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res


if __name__ == '__main__':
    tree_str = "[5,4,8,11,null,13,4,7,2,null,null,5,1]"
    root = deserialize(tree_str)
    target = 22
    printTree(root)

    solution = Solution()
    print(solution.pathSum(root, target))
