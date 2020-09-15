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
from utils import generateList, printList


class Solution(object):
    def reverseList_1(self, head):
        """
        双指针迭代
        时间复杂度：O(N)，N 为链表节点的个数
        空间复杂度：O(1)
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

    def reverseList_2(self, head):
        """
        递归解法
        时间复杂度：O(N)，N 为链表节点的个数
        空间复杂度：O(N)，递归系统栈
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head is None or head.next is None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList_2(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


if __name__ == '__main__':
    solution = Solution()

    head = generateList([1, 2, 3, 4, 5])
    printList(solution.reverseList_1(head))

    head = generateList([1, 2, 3, 4, 5])
    printList(solution.reverseList_2(head))
