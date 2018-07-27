"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

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
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        li = [ch for ch in s]
        sub = []
        length = 1
        for ch in li:
            if ch in sub:
                length = len(sub) if len(sub) > length else length
                sub = sub[sub.index(ch) + 1:]
                sub.append(ch)
            else:
                sub.append(ch)

        return max(length, len(sub))


def main():
    """Summary"""
    sol = Solution()
    test_cases = ['abcabcbb', 'bbbbb', 'pwwkew', 'dvdf']
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.lengthOfLongestSubstring(case)))


if __name__ == '__main__':
    main()
