# -*- coding: utf-8 -*-
"""
剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        时间复杂度 O(N)： 其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），
        最大为 N （退化为链表）。
        空间复杂度 O(1)： 使用常数大小的额外空间。
        :param root:
        :param p:
        :param q:
        :return:
        """
        if p.val > q.val: p, q = q, p  # 保证 p.val < q.val
        while root:
            if root.val < p.val:  # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else:
                break
        return root

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        时间复杂度 O(N)： 其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），
        最大为 N （退化为链表）。
        空间复杂度 O(N)： 最差情况下，即树退化为链表时，递归深度达到树的层数 N 。
        :param root:
        :param p:
        :param q:
        :return:
        """
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor_2(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor_2(root.left, p, q)
        return root


