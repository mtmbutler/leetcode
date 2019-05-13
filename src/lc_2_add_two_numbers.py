"""
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked
list.

You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    
class LinkedList:
    """A helper class for running test cases."""
    def __init__(self, arg):
        """arg can be a list or just the first node."""
        if isinstance(arg, ListNode) or isinstance(arg, LinkedList):
            self.val = arg.val
            self.next = arg.next
        elif isinstance(arg, list):
            first_node = ListNode(arg[0])
            nodes = [first_node]
            for i, v in enumerate(arg[1:]):
                n = ListNode(v)
                nodes[i].next = n
                nodes.append(n)

            # Set self to the first node
            self.val = first_node.val
            self.next = first_node.next
        else:
            raise TypeError("arg must be list or ListNode.")

    def __eq__(self, other):
        return self.to_list() == other.to_list()

    def to_list(self):
        node = self
        li = [node.val]
        while node.next is not None:
            node = node.next
            li.append(node.val)
        return li


def ll_to_list(node):
    ret = [str(node.val)]
    while node.next is not None:
        node = node.next
        ret.append(str(node.val))
    return ret


def list_to_ll(li):
    nodes = [ListNode(li[0])]
    for i, v in enumerate(li[1:]):
        n = ListNode(v)
        nodes[i].next = n
        nodes.append(n)
    return nodes[0]


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        li_1 = ll_to_list(l1)
        li_2 = ll_to_list(l2)

        # Reverse and add
        num = int(''.join(li_1[::-1])) + int(''.join(li_2[::-1]))

        # Split back into linked list
        return list_to_ll([int(i) for i in list(str(num))[::-1]])


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([LinkedList([2, 4, 3]), LinkedList([5, 6, 4])],
         LinkedList([7, 0, 8])),
        ([LinkedList([4, 3]), LinkedList([5, 6, 4])],
         LinkedList([9, 9, 4])),
    )
    for args, out in test_cases:
        assert LinkedList(sol.addTwoNumbers(*args)) == out
