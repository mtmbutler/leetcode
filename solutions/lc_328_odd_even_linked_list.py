"""
https://leetcode.com/problems/odd-even-linked-list/

Given a singly linked list, group all odd nodes together followed by the
even nodes. Please note here we are talking about the node number and
not the value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

The relative order inside both the even and odd groups should remain as
it was in the input.

The first node is considered odd, the second node even and so on ...
"""


from utils import ListNode, node_from_iterable as nodify


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """Re-orders a linked list to be all odd elements first.

        This is a linear time, in-place solution using two pointers.

        Here is a visual example of how this algorithm works. Key:
            odd_cur = &
            even_cur = $

        Input: 1->2->3->4->5->NULL

        # Setup
        odd_cur = head
        even_cur = odd_cur.next
        even_first = even_cur

        1->2->3->4->5->NULL
        &  $

        odd_cur.next = even_cur.next
        odd_cur = odd_cur.next

           2 $
           |
           v
        1->3->4->5->NULL
           &

        even_cur.next = odd_cur.next
        even_cur = even_cur.next

              2
              |
              v
        1->3->4->5->NULL
           &  $

        odd_cur.next = even_cur.next
        odd_cur = odd_cur.next

           2->4 $
              |
              v
        1->3->5->NULL
              &

        even_cur.next = odd_cur.next  # Now even_cur.next is None

           2->4->NULL
              $

        1->3->5
              &

        odd_cur.next = even_first  # Now we've achieved the desired state

        1->3->5->2->4->NULL
              &     $

        return head
        """
        if not hasattr(head, 'next') or head.next is None:
            return head

        # Setup
        odd_cur = head
        even_cur = odd_cur.next
        even_first = even_cur

        while True:
            # Change the current odd element to point to the next odd
            # element, then move the odd pointer to the next odd
            # element.
            odd_cur.next = even_cur.next
            if odd_cur.next is None:
                odd_cur.next = even_first
                break
            odd_cur = odd_cur.next

            # Change the current even element to point to the next even
            # element, then move the even pointer to the next even
            # element.
            even_cur.next = odd_cur.next
            if even_cur.next is None:
                odd_cur.next = even_first
                break
            even_cur = even_cur.next

        return head


if __name__ == '__main__':
    sol = Solution()

    test_cases = (
        [[], []],
        [None, None],
        [nodify([1]), nodify([1])],
        [nodify([1, 2]), nodify([1, 2])],
        [nodify([1, 2, 3, 4, 5]), nodify([1, 3, 5, 2, 4])],
        [nodify([2, 1, 3, 5, 6, 4, 7]), nodify([2, 3, 6, 7, 1, 5, 4])]
    )
    for arg, out in test_cases:
        result = sol.oddEvenList(arg)
        print(arg, result, out)
        assert result == out
