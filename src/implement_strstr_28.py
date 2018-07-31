"""
https://leetcode.com/problems/implement-strstr/description/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        elif needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    return i


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [('hello', 'll'),
                  ('aaaaa', 'bba'),
                  ('', 'foo'),
                  ('bar', ''),
                  ('', ''),
                  ('ayesyes', 'yes')]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.strStr(*case,)))


if __name__ == '__main__':
    main()
