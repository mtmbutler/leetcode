"""
https://leetcode.com/problems/longest-palindrome/

Given a string which consists of lowercase or uppercase letters, find
the length of the longest palindromes that can be built with those
letters.

This is case sensitive, for example "Aa" is not considered a palindrome
here.

Note:

Assume the length of given string will not exceed 1,010.

Example:
Input:

"abccccdd"
Output:

7
Explanation:

One longest palindrome that can be built is "dccaccd", whose length is
7.
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)  # O(N)
        max_len = 0
        found_center = False
        for ch, count in c.items():  # O(N) in worst case
            if count == 1 and not found_center:
                max_len += 1
                found_center = True
            elif count > 1:
                max_len += count
                if found_center:
                    max_len -= count % 2
                else:
                    if count % 2 == 1:  # Odd
                        found_center = True
        return max_len


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ["abccccdd", 7],
        ["aabbccdd", 8],
        ["aaabbc", 5],
        ["cbbaaa", 5],
        ["aaabb", 5],
        ["bbaaa", 5],
        ["", 0],
        ["a", 1]
    )
    for arg, out in test_cases:
        result = sol.longestPalindrome(arg)
        print(arg, result, out)
        assert result == out
