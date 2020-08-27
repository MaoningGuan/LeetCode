# -*- coding: utf-8 -*-
"""
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

 

提示：

节点总数 <= 10000
"""
from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth_1(self, root: TreeNode) -> int:
        """
        深度优先搜索后序遍历二叉树的各个节点（DFS）
        时间复杂度 O(N) ： N 为树的节点数量，计算树的深度需要遍历所有节点。
        空间复杂度 O(N) ： 最差情况下（当树退化为链表时），递归深度可达到 N 。
        :param root:
        :return:
        """
        if not root: return 0
        return max(self.maxDepth_1(root.left), self.maxDepth_1(root.right)) + 1

    def maxDepth_2(self, root: TreeNode) -> int:
        """
        广度优先搜索层次遍历二叉树的各个节点（BFS）
        时间复杂度 O(N) ： N 为树的节点数量，计算树的深度需要遍历所有节点。
        空间复杂度 O(N) ： 最差情况下（当树平衡时），队列 queue 同时存储 N/2 个节点。
        :param root:
        :return:
        """
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res


if __name__ == '__main__':
    nodes = "[3,9,20,null,null,15,7]"
    root = deserialize(nodes)

    solution = Solution()
    print(solution.maxDepth_1(root))
    print(solution.maxDepth_2(root))
