"""
https://leetcode.com/problems/longest-palindromic-substring

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
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    @staticmethod
    def find_all(li, x):
        return [i for i, val in enumerate(li) if val == x]

    def longestPalindrome(self, s):
        if self.is_palindrome(s):  # Already a palindrome
            return s
        if not s:
            return ''
        longest = s[0]
        for i, ch in enumerate(s):
            indices = self.find_all(s, ch)
            for j in indices[::-1]:
                if j <= i:  # Don't look backwards
                    break
                if j - i + 1 <= len(longest):  # Ignore shorter ones
                    break
                check = s[i:j + 1]
                if self.is_palindrome(check):
                    longest = check
        return longest


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ('abcda', 'a'),
        ('ac', 'a'),
        ('hohoh', 'hohoh'),
        ('babad', 'bab'),
        ('cbbd', 'bb'))
    for arg, out in test_cases:
        result = sol.longestPalindrome(arg)
        print(arg, result, out)
        assert result == out
