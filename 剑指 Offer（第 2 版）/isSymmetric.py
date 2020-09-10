# -*- coding: utf-8 -*-
"""
剑指 Offer 28. 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3



示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false


限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
"""
from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recur(L, R):
            # 两个节点都为空
            if not L and not R: return True
            # 两个节点中有一个为空或者两个节点的值不相等
            if not L or not R or L.val != R.val: return False
            # 归的比较 left.left 和 right.right，递归比较 left.right 和 right.left
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right)


if __name__ == '__main__':
    root = deserialize("[1,2,2,3,4,4,3]")
    solution = Solution()
    print(solution.isSymmetric(root))

