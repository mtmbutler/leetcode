"""
https://leetcode.com/problems/reverse-integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231,  231 − 1]. For
the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        # Create a list of x's digits
        digits = str(x)

        # Control for negative numbers
        neg = digits[0] == '-'
        if neg:
            digits = digits[1:]

        # Reverse the integer
        rvrsd = int(digits[::-1]) * (-1 if neg else 1)

        # Return the reversed number, conditional on overflow
        if not -(2**31) <= rvrsd <= 2**31:
            return 0
        else:
            return rvrsd


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        (123, 321),
        (-123, -321),
        (120, 21))
    for arg, out in test_cases:
        result = sol.reverse(arg)
        print(arg, result, out)
        assert result == out
