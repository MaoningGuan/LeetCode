# -*- coding: utf-8 -*-
"""
功能函数
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l: List[int]) -> ListNode:
    """
    由list来构造链表
    :param l:
    :return:
    """
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    """
    打印链表
    :param l:
    :return:
    """
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root: TreeNode) -> List[List[int]]:
    """
    按层打印二叉树，包含空子节点
    :param root:
    :return:
    """
    import collections
    if not root:
        return []

    res, q = [], collections.deque()
    q.append(root)
    while q:
        # 输出是二维数组
        temp = []
        for x in range(len(q)):
            node = q.popleft()
            if node:
                temp.append(node.val)
            else:
                temp.append(None)
                continue
            if node.left:
                q.append(node.left)
            else:
                q.append(None)
            if node.right:
                q.append(node.right)
            else:
                q.append(None)
        res.append(temp)
    # 去掉最后一层的全空子节点
    res = res[:-1]
    print(res)
    return res


def printTree_2(root: TreeNode) -> List[List[int]]:
    """
    按层打印二叉树，不包含空子节点
    :param root:
    :return:
    """
    import collections
    if not root:
        return []

    res, q = [], collections.deque()
    q.append(root)
    while q:
        # 输出是二维数组
        temp = []
        for x in range(len(q)):
            node = q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(temp)
    print(res)
    return res