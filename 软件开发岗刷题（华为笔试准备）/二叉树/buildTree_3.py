# -*- coding: utf-8 -*-
"""
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""
from typing import List
from utils import printTree, printTree_2
from itertools import chain


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic, self.po = {}, postorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(len(postorder) - 1, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right: return  # 终止条件：中序遍历为空
        print(pre_root)
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root - (in_right - i) - 1, in_left, i - 1)  # 开启左子树的下层递归
        root.right = self.recur(pre_root - 1, i + 1, in_right)  # 开启右子树的下层递归
        return root  # 返回根节点，作为上层递归的左（右）子节点


if __name__ == '__main__':
    # preorder = [3, 9, 20, 15, 7]
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    res_TreeNode = solution.buildTree(postorder, inorder)
    res = printTree(res_TreeNode)
    print(list(chain(*res)))
