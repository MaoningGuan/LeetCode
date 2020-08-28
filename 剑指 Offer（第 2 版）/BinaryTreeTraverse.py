# -*- coding: utf-8 -*-
"""
----------使用不同方式来遍历二叉树-----------
四种主要的遍历思想为：
前序遍历：根结点 ---> 左子树 ---> 右子树
中序遍历：左子树---> 根结点 ---> 右子树
后序遍历：左子树 ---> 右子树 ---> 根结点
层次遍历：只需按层次遍历即可

例如，求下面二叉树的各种遍历
                1
              /   \
             2     3
            / \     \
           4   5     6
              / \
             7   8
前序遍历：1  2  4  5  7  8  3  6

中序遍历：4  2  7  5  8  1  3  6

后序遍历：4  7  8  5  2  6  3  1

层次遍历：1  2  3  4  5  6  7  8
"""
from typing import List

from utils import TreeNode, deserialize


def preOrderTraverse(root: TreeNode) -> List[int]:
    """
    深度优先（递归）——前序遍历：根结点 ---> 左子树 ---> 右子树
    时间复杂度：O(N)
    空间复杂度：O(N)
    :param root:
    :return:
    """
    nodes = []
    if not root: return []
    nodes.append(root.val)
    nodes_left = preOrderTraverse(root.left)
    if nodes_left:
        nodes += nodes_left
    nodes_right = preOrderTraverse(root.right)
    if nodes_right:
        nodes += nodes_right
    return nodes


def inOrderTraverse(root: TreeNode) -> List[int]:
    """
    深度优先（递归）——中序遍历：左子树---> 根结点 ---> 右子树
    时间复杂度：O(N)
    空间复杂度：O(N)
    :param root:
    :return:
    """
    nodes = []
    if not root:
        return []

    nodes_left = inOrderTraverse(root.left)
    if nodes_left:
        nodes += nodes_left

    nodes.append(root.val)

    nodes_right = inOrderTraverse(root.right)
    if nodes_right:
        nodes += nodes_right

    return nodes


def postOrderTraverse(root: TreeNode) -> List[int]:
    """
    深度优先（递归）——后序遍历：左子树 ---> 右子树 ---> 根结点
    时间复杂度：O(N)
    空间复杂度：O(N)
    :param root:
    :return:
    """
    nodes = []
    if not root:
        return []

    nodes_left = postOrderTraverse(root.left)
    if nodes_left:
        nodes += nodes_left

    nodes_right = postOrderTraverse(root.right)
    if nodes_right:
        nodes += nodes_right

    nodes.append(root.val)
    return nodes


def levelTraverse(root: TreeNode) -> List[int]:
    """
    广度优先搜索（队列）——层次遍历：按层遍历二叉树
    时间复杂度：O(N)
    空间复杂度：O(N)
    :param root:
    :return:
    """
    queue = [root]
    res = []
    while queue:
        nodes = []
        for node in queue:
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        queue = nodes
    return res


if __name__ == '__main__':
    tree_nodes = "[1,2,3,4,5,null,6,null,null,7,8,null,null]"
    root = deserialize(tree_nodes)
    print('前序遍历：', preOrderTraverse(root))
    print('中序遍历：', inOrderTraverse(root))
    print('后序遍历：', postOrderTraverse(root))
    print('层次遍历：', levelTraverse(root))
