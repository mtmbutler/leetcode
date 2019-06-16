from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterable


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other: 'ListNode'):
        return self.val == other.val and self.next == other.next

    def __str__(self):
        next_ = str(self.next) if self.next is not None else 'NULL'
        return f"{self.val}->{next_}"


def node_from_iterable(it: 'Iterable'):
    if not it:
        return
    nodes = [ListNode(i) for i in it]
    if len(nodes) > 1:
        for i, node in enumerate(nodes[:-1]):
            node.next = nodes[i + 1]

    return nodes[0]
