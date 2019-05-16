"""
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner
as shown in the figure.

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:

Assume that the total area is never beyond the maximum possible value of
int.
"""


# Just used this to think about the solution
class Rectangle:
    def __init__(self, a, b, c, d):
        """A rectangle on a coordinate plane.

        Bottom left corner is (a, b) and top right is (c, d).
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @property
    def area(self):
        return (self.d - self.b) * (self.c - self.a)

    def overlap_area(self, other):
        # Horizontal overlap
        wide = min(self.c, other.c) - max(self.a, other.a)

        # Vertical overlap
        long = min(self.d, other.d) - max(self.b, other.b)

        return wide * long


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        a_1 = (D - B) * (C - A)
        a_2 = (H - F) * (G - E)
        a_overlap = (
                max((min(C, G) - max(A, E)), 0)
                * max((min(D, H) - max(B, F)), 0))
        return a_1 + a_2 - a_overlap


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([-3, 0, 3, 4, 0, -1, 9, 2], 45),  # Corner overlap
        ([0, 0, 2, 2, 2, 2, 4, 4], 8),  # No overlap
        ([0, 0, 2, 2, -1, 1, 3, 3], 10),  # Top overlap
        ([0, 0, 1, 1, -1, -1, 2, 2], 9),  # Full overlap
        ([-2, -2, 2, 2, 3, 3, 4, 4], 17))  # Spaced apart
    for args, out in test_cases:
        result = sol.computeArea(*args)
        print(args, result, out)
        assert result == out
