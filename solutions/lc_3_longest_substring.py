"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that
    the answer must be a substring, "pwke" is a subsequence and not a
    substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        sub = []
        length = 1
        for ch in s:
            if ch in sub:
                length = len(sub) if len(sub) > length else length
                sub = sub[sub.index(ch) + 1:]
                sub.append(ch)
            else:
                sub.append(ch)

        return max(length, len(sub))


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('dvdf', 3),
        ('', 0),
        ('a', 1))
    for arg, out in test_cases:
        assert sol.lengthOfLongestSubstring(arg) == out
