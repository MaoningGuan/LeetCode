# -*- coding: utf-8 -*-
"""
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000
"""
from typing import List
from utils import generateList, printList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint_1(self, head: ListNode) -> List[int]:
        return self.reversePrint_1(head.next) + [head.val] if head else []

    def reversePrint_2(self, head: ListNode) -> List[int]:
        stack = list()
        while head:
            stack.append(head.val)
            head = head.next
        stack.reverse()
        # return stack
        return stack[::-1]


if __name__ == '__main__':
    head = generateList([1, 3, 2, 5, 9, 0])
    solution = Solution()
    print(solution.reversePrint_1(head))
    printList(head)
    print(solution.reversePrint_2(head))
    printList(head)

