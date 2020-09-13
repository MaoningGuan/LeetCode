# -*- coding: utf-8 -*-
"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
from utils import generateList, printList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs_1(self, head: ListNode) -> ListNode:
        """
        方法一：递归
        时间复杂度：O(N)，其中 N 指的是链表的节点数量。
        空间复杂度：O(N)，递归过程使用的堆栈空间。
        :param head:
        :return:
        """
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs_1(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node

    def swapPairs_2(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


if __name__ == '__main__':
    head = generateList([1, 2, 3, 4, 5])
    solution = Solution()
    printList(solution.swapPairs_1(head))
    head = generateList([1, 2, 3, 4, 5])
    printList(solution.swapPairs_2(head))

