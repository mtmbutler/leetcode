"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(set(s)) == len(list(s)):
            return s[0]

        


def main():
    sol = Solution()
    test_cases = ['babad', 'cbbd']
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.longestPalindrome(case)))

if __name__ == '__main__':
    main()
