"""
TODO
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def ll_sort(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val <= l2.val:
            return l1, l2
        else:
            return l2, l1

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        here, there = self.ll_sort(l1, l2)
        start = here

        while here.next is not None:
            here.next, there = self.ll_sort(here.next, there)
            here = here.next

        return start


def main():
    """Summary
    """
    sol = Solution()
    c = ListNode(4)
    b = ListNode(1, c)
    a = ListNode(1, b)
    z = ListNode(4)
    y = ListNode(3, z)
    x = ListNode(1, y)
    test_cases = [[a, x]]
    for case in test_cases:
        x = sol.mergeTwoLists(*case)
        print(x.val)
        while x.next is not None:
            x = x.next
            print(x.val)


if __name__ == '__main__':
    main()
