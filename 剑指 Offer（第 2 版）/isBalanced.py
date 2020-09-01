# -*- coding: utf-8 -*-
"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""
from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced_1(self, root: TreeNode) -> bool:
        """
        方法一：后序遍历 + 剪枝 （从底至顶）
        时间复杂度 O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。
        空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。
        :param root:
        :return:
        """
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

    def isBalanced_2(self, root: TreeNode) -> bool:
        """
        时间复杂度 O(NlogN)
        空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。
        :param root:
        :return:
        """
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced_2(root.left) and self.isBalanced_2(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1


if __name__ == '__main__':
    root = deserialize("[3,9,20,null,null,15,7]")
    solution = Solution()
    print(solution.isBalanced_1(root))
    print(solution.isBalanced_2(root))

