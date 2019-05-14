"""
https://leetcode.com/problems/valid-parentheses

Given a string containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        if not s:
            return True  # Empty string is valid

        openers = ('[', '(', '{')
        closers = (']', ')', '}')
        for opener, closer in zip(openers, closers):
            if s.count(opener) != s.count(closer):
                return False  # Early exit if any mismatches
        if any(ch not in openers + closers for ch in s):
            return False  # Early exit for invalid characters

        last_openers = [(False, False, False)]
        for ch in s:
            if ch in openers:
                last_openers.append(tuple(ch == i for i in openers))
            elif ch in closers:
                if tuple(ch == i for i in closers) != last_openers[-1]:
                    return False
                last_openers.pop(-1)
        return True


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ('', True),
        ('(', False),
        ('(()', False),
        ('{', False),
        ('[', False),
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
        ('{[()]}', True),
        ('{[]()}', True),
        ('{[]()}}', False),
        ('({[]()})', True))
    for arg, out in test_cases:
        result = sol.isValid(arg)
        print(arg, result, out)
        assert result == out
