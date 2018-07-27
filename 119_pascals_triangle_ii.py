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

import math


def choose(a, b):
    x = max(a, b)
    y = min(a, b)
    return int(math.factorial(x) / math.factorial(y)
               / math.factorial(x - y))


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        print(str([i for i in range(rowIndex + 1)]))
        return [choose(i, rowIndex + 1 - i)
                for i in range(rowIndex + 1)]


def main():
    sol = Solution()
    test_cases = [0, 1, 2, 3, 4]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.getRow(case)))


if __name__ == '__main__':
    main()
