"""
https://leetcode.com/problems/longest-common-prefix/description/

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
        """
        :type strs: List[str]
        :rtype: str
        """
        # Catch empty case
        if not strs:
            return ""

        # Get smallest word length to know the longest possible prefix
        shortest_length = len(min(strs, key=len))

        # Iterate over prefices to see matches
        longest_prefix = ""
        for i in range(shortest_length):
            prefices = [word[:i + 1] for word in strs]
            prfcs_match = len(set(prefices)) == 1
            if prfcs_match:
                longest_prefix = prefices[0]
        return longest_prefix


def main():
    sol = Solution()
    test_cases = [[],
                  ["a"],
                  ["ababklaj;lasbn"],
                  ["c", "c"],
                  ["", "hi"],
                  ["flower", "flow", "flight"],
                  ["dog", "racecar", "car"]]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.longestCommonPrefix(case)))


if __name__ == '__main__':
    main()
