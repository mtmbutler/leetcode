"""
https://leetcode.com/problems/palindrome-number

Determine whether an integer is a palindrome. An integer is a palindrome
when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x):
        if 0 <= x < 10:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        flipped = 0
        while x > flipped:
            flipped = flipped * 10 + (x % 10)
            x //= 10
            if flipped in (x, x // 10):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (632236, True),
        (163, False),
        (112, False),
        (412, False),
        (634, False),
        (679976, True),
        (108, False),
        (822, False),
        (348, False),
        (658856, True),
        (132, False))
    for arg, out in test_cases:
        result = sol.isPalindrome(arg)
        print(arg, result, out)
        assert result == out
