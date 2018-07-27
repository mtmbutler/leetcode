"""
https://leetcode.com/problems/add-two-numbers/description/

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

        num = int(''.join(li_1[::-1])) + int(''.join(li_2[::-1]))
        print(num)
        li = [ch for ch in str(num)]
        print(li)
        li = li[::-1]
        print(li)
        return list_to_ll(li)

# def main():
#     """Summary
#     """
#     sol = Solution()
#     test_cases = [test_one, test_two]
#     for case in test_cases:
#         print('Input: {}\nOutput: {}\n------------'
#               .format(case, sol.methodName(case)))


# if __name__ == '__main__':
#     main()
