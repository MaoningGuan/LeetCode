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
