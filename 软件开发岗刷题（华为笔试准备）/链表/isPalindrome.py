# -*- coding: utf-8 -*-
"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from utils import generateList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome_1(self, head: ListNode) -> bool:
        """
        方法一：将值复制到数组中后用双指针法
        时间复杂度：O(n)O(n)，其中 nn 指的是链表的元素个数。
        第一步： 遍历链表并将值复制到数组中，O(n)O(n)。
        第二步：双指针判断是否为回文，执行了 O(n/2) 次的判断，即 O(n)O(n)。
        总的时间复杂度：O(2n) = O(n)O(2n)=O(n)。
        :param self:
        :param head:
        :return:
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    def isPalindrome_2(self, head: ListNode) -> bool:
        """
        方法二、递归
        时间复杂度：O(n)，其中 n 指的是链表的大小。
        空间复杂度：O(n)，其中 n 指的是链表的大小。
        :param head:
        :return:
        """

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

    def isPalindrome_3(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous



if __name__ == '__main__':
    head = generateList([1, 2, 3, 3, 2, 1])

    solution = Solution()
    print(solution.isPalindrome_1(head))
    print(solution.isPalindrome_2(head))
    print(solution.isPalindrome_3(head))

