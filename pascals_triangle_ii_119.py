"""
https://leetcode.com/problems/pascals-triangle-ii/description/

Given a non-negative index k where k ≤ 33, return the kth index row of
the Pascal's triangle.

Note that the row index starts from 0.

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

In Pascal's triangle, each number is the sum of the two numbers directly
above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
"""

from math import factorial as fac


def choose(a, b):
    assert a >= b
    return round(fac(a) / fac(b) / fac(a - b))


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [choose(rowIndex, i)
                for i in range(rowIndex + 1)]


def main():
    sol = Solution()
    test_cases = [24]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.getRow(case)))


if __name__ == '__main__':
    main()
