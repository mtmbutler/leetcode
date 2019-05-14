"""
https://leetcode.com/problems/longest-common-prefix

Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # Catch empty case
        if not strs:
            return ""

        # Get smallest word length to know the longest possible prefix
        shortest_str = min(strs, key=len)

        # Iterate over prefices to see matches
        longest_prefix = []
        for i, ch in enumerate(shortest_str):
            different = False
            for s in strs:
                if s[i] != ch:
                    different = True
                    break
            if different:
                break
            longest_prefix.append(ch)

        return ''.join(longest_prefix)


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([], ''),
        (['a'], 'a'),
        (['ababklaj;lasbn'], 'ababklaj;lasbn'),
        (['c', 'c'], 'c'),
        (['', 'hi'], ''),
        (['flower', 'flow', 'flight'], 'fl'),
        (['dog', 'racecar', 'car'], ''))
    for arg, out in test_cases:
        result = sol.longestCommonPrefix(arg)
        print(arg, result, out)
        assert result == out
