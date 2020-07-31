# -*- coding: utf-8 -*-
"""
206. 反转链表
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


class Solution:
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        """
        递归解法
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList_recursive(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空(如：5 -> 4 -> 3 -> 2 <-> 1)
        # if head.val == 1:
        #     head.next = None
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

    def reverseList_iterate(self, head: ListNode) -> ListNode:
        """
        迭代解法
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # pre, cur.next, cur = cur, pre, cur.next
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    solution = Solution()
    nodes = [1, 2, 3, 4, 5]
    linked_list = generateList(nodes)
    reversed_link = solution.reverseList_iterate(linked_list)
    printList(reversed_link)

