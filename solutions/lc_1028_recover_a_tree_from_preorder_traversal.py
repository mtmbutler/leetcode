"""
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth
of this node), then we output the value of this node.  (If the depth of
a node is D, the depth of its immediate child is D+1.  The depth of the
root node is 0.)

If a node has only one child, that child is guaranteed to be the left
child.

Given the output S of this traversal, recover the tree and return its
root.

Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Note:

The number of nodes in the original tree is between 1 and 1000.

Each node will have a value between 1 and 10^9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right)

    def __str__(self):
        if self.left is None and self.right is None:
            vals = [self.val]
        else:
            vals = [self.val, self.left, self.right]
        return ', '.join([str(i) for i in vals])


class TreeCrawler:
    def __init__(self, root):
        self.root = root
        self.cur_node = root
        self.parents = []  # node path to cur_node from root

    def new_branch(self, val):
        if self.cur_node.left is None:
            self.cur_node.left = TreeNode(val)
        else:
            self.cur_node.right = TreeNode(val)

    def move_down(self, left=True):
        self.parents.append(self.cur_node)
        if left:
            self.cur_node = self.cur_node.left
        else:
            self.cur_node = self.cur_node.right

    def move_to_root(self):
        self.cur_node = self.root
        self.parents = []

    def move_up(self, tiers=1):
        for __ in range(tiers):
            self.cur_node = self.parents.pop(-1)


class Solution:
    @staticmethod
    def split_into_list(s):
        li = [[]]
        last = ''
        for ch in s:
            if ch == '-' and last != '-':
                li.append([ch])
            else:
                li[-1].append(ch)
            last = ch
        li = [''.join(subli) for subli in li]
        return li

    def recoverFromPreorder(self, S):
        # Convert to list and create root and crawler
        li = self.split_into_list(S)
        root = TreeNode(int(li[0]))
        crawler = TreeCrawler(root)

        # Iterate through nodes
        prev_level = 0
        for node in li[1:]:
            level = node.count('-')
            val = int(node.replace('-', ''))

            # Move the crawler according to level, then add new branch
            if level <= prev_level:
                crawler.move_up(tiers=max(prev_level - level + 1, 0))
            else:
                pass  # TODO
            crawler.new_branch(val)

        return root


if __name__ == '__main__':
    sol = Solution()

    # Tree 1
    tn_1 = TreeNode(1)
    tn_1.left = TreeNode(2)
    tn_1.left.left = TreeNode(3)
    tn_1.left.right = TreeNode(4)
    tn_1.right = TreeNode(5)
    tn_1.right.left = TreeNode(6)
    tn_1.right.right = TreeNode(7)
    print(tn_1)

    # Tree 2
    tn_2 = TreeNode(1)
    tn_2.left = TreeNode(2)
    tn_2.left.left = TreeNode(3)
    tn_2.left.left.left = TreeNode(4)
    tn_2.right = TreeNode(5)
    tn_2.right.left = TreeNode(6)
    tn_2.right.left.left = TreeNode(7)
    print(tn_2)

    # Tree 3
    tn_3 = TreeNode(1)
    tn_3.left = TreeNode(401)
    tn_3.left.left = TreeNode(349)
    tn_3.left.left.left = TreeNode(90)
    tn_3.left.right = TreeNode(88)
    print(tn_2)

    test_cases = (
        ('1-2--3--4-5--6--7', tn_1),
        ('1-2--3---4-5--6---7', tn_2),
        ('1-401--349---90--88', tn_3)
    )
    for arg, out in test_cases:
        result = sol.recoverFromPreorder(arg)
        print(arg, result, out)
        assert result == out
