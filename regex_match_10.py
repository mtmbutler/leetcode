"""
https://leetcode.com/problems/regular-expression-matching/description/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # No regex
        if '.' not in p and '*' not in p:
            return s == p

        # Split p into arrays that contain one character each
        # i.e. 'fo*ba*r' -> [['f'],['o','*'],['b'],['a','*'],['r']]
        p_spl = []
        ind = -1
        for ch in p:
            if ch != '*':
                p_spl.append([])
                ind += 1
            p_spl[ind].append(ch)

        # Split s into an array
        s_spl = [ch for ch in s]

        # Determine match
        match = True
        i = 0
        while match:
            if len(p_spl[i]) == 1:  # Just a letter
                match = (p_spl[i][0] == s_spl[i])
                i += 1
            elif len(p_spl[i]) == 2:  # Has an asterisk
                raise NotImplementedError
            else:
                print(p_spl)
                raise IndexError

        return match


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [['aa', 'a'],
                  ['aa', 'a*'],
                  ['ab', '.*'],
                  ['aab', 'c*a*b'],
                  ['mississippi', 'mis*is*p*.']]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.isMatch(*case)))


if __name__ == '__main__':
    main()
