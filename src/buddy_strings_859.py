"""
https://leetcode.com/contest/weekly-contest-90/problems/buddy-strings/

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) != len(list(A))

        # Count differences
        diff = []
        for i, ch in enumerate(A):
            if ch != B[i]:
                diff.append([i, ch, B[i]])

        # False if not two differences
        if len(diff) != 2:
            return False

        # Check if swapping can fix the difference
        if (diff[0][1] == diff[1][2]
                and diff[0][2] == diff[1][1]):
            return True
        return False


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [['ab', 'ba'], ['ab', 'ab'], ['aa', 'aa'],
                  ['aaaaaaabc', 'aaaaaaacb'], ['', 'aa']]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.buddyStrings(*case)))


if __name__ == '__main__':
    main()
