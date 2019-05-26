"""
https://leetcode.com/problems/string-without-aaa-or-bbb/

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
letters;

The substring 'aaa' does not occur in S;

The substring 'bbb' does not occur in S.

Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:
Input: A = 4, B = 1
Output: "aabaa"

Note:

0 <= A <= 100

0 <= B <= 100

It is guaranteed such an S exists for the given A and B.
"""

# 1 too many A's:
# 5, 1 -> aabaaa
# 7, 2 -> aabaabaaa
# 9, 3 -> aabaabaabaaa
# 2B + 3, B

# Strategy 1: alternate (abababaa)
# Works for B <= A <= B + 2

# Strategy 2: double up (aabaabaabaabaabaabb)
# Works for 2B - 2 <= A <= 2B + 2

# Strategy 3:

# 12, 7 = ok
# 12, 8 = bad


class Solution:
    def str_wo_3(self, A: int, B: int) -> str:
        """The below function, but requires A >= B.

        The problem guarantees a legal solution, implying A < 2B + 3:
            1 too many A's:
            5, 1 -> aabaaa
            7, 2 -> aabaabaaa
            9, 3 -> aabaabaabaaa
            2B + 3, B

        We can use one of two strategies:
            Strategy 1: alternate (abababaa)
            Works for B <= A <= B + 2

            Strategy 2: double up (aabaabaabaabaabaabb)
            Works for 2B - 2 <= A <= 2B + 2

        For A in (B + 2, 2B - 2), we can punt by alternating, and
        eventually A and B will converge into one of the valid ranges.
        """
        li = []
        while A + B > 3 and A * B > 1:
            if A > 2 * B - 3:
                li.append('aab')
                A -= 2
                B -= 1
            else:
                li.append('ab')
                A -= 1
                B -= 1
        li.append('a' * A + 'b' * B)
        return ''.join(li)

    def strWithout3a3b(self, A: int, B: int) -> str:
        if A >= B:
            return self.str_wo_3(A, B)
        else:
            s = self.str_wo_3(B, A)
            # Swap the A's and B's
            return s.replace('a', 'c').replace('b', 'a').replace('c', 'b')


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        (1, 2),
        (2, 1),
        (4, 1),
        (0, 0),
        (0, 1),
        (1, 0),
        (100, 99),
        (1, 4),
        (10, 12),
        (100, 60)
    )
    for A, B in test_cases:
        result = sol.strWithout3a3b(A, B)
        print(A, B, result)
        assert len(result) == A + B
        assert result.count('a') == A
        assert result.count('b') == B
        assert 'aaa' not in result
        assert 'bbb' not in result
