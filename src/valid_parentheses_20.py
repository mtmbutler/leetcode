"""
https://leetcode.com/problems/valid-parentheses/description/

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
        """
        :type s: str
        :rtype: bool
        """
        if (s.count('[') != s.count(']')
                or s.count('(') != s.count(')')
                or s.count('{') != s.count('}')):
            return False
        openers = ['[', '(', '{']
        closers = [']', ')', '}']
        last_openers = [[False, False, False]]
        for ch in s:
            if ch not in openers + closers:
                return False
            elif ch in openers:
                last_openers.append([ch == i for i in openers])
            elif ch in closers:
                if [ch == i for i in closers] != last_openers[-1]:
                    return False
                last_openers = last_openers[:-1]

        return True


def main():
    """Summary
    """
    sol = Solution()
    test_cases = ['', '(', '(()', '{', '[', '()', '()[]{}', '(]', '([)]',
                  '{[]}', '{[()]}', '{[]()}', '{[]()}}', '({[]()})']
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.isValid(case)))


if __name__ == '__main__':
    main()
