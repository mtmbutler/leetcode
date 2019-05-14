"""
https://leetcode.com/contest/weekly-contest-90/problems/score-of-parentheses/

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
"""


class Solution:

    """Summary
    """

    def methodName(self):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # TODO


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [test_one, test_two]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.methodName(case)))


if __name__ == '__main__':
    main()
