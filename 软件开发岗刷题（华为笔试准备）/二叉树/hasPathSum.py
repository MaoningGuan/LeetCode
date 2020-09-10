# -*- coding: utf-8 -*-
"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

通过次数133,850提交次数261,775
"""
import collections

from utils import TreeNode, deserialize


class Solution:
    def hasPathSum_1(self, root: TreeNode, sum: int) -> bool:
        """
        方法一：广度优先搜索（队列）
        时间复杂度：O(N)，其中 N 是树的节点数。对每个节点访问一次。
        空间复杂度：O(N)，其中 N 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False

    def hasPathSum_2(self, root: TreeNode, sum: int) -> bool:
        """
        深度优先搜索（递归）
        时间复杂度：O(N)O(N)，其中 NN 是树的节点数。对每个节点访问一次。

        空间复杂度：O(H)，其中 H 是树的高度。空间复杂度主要取决于递归时栈空间的开销，
        最坏情况下，树呈现链状，空间复杂度为 O(N)。平均情况下树的高度与节点数的对数正相关，空间复杂度为 O(logN)。
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

