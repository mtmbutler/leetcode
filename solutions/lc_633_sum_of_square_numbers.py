"""
https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer c, your task is to decide whether there're
two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False


"""
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Get upper bound of a/b: O(1)
        sqrt = math.sqrt(c)
        if sqrt % 1 == 0:  # If c is a perf square, sqrt(c)^2 + 0^2 = c
            return True
        upper = math.ceil(sqrt)

        # Put squares in a hash map for quick lookup: O(N)
        squares = set(n**2 for n in range(upper + 1))

        # Iterate: O(N)
        for s in squares:
            if c - s in squares:  # Lookup in hash map: O(1)
                return True
        return False


if __name__ == '__main__':
    sol = Solution()

    # Check complexity
    test_cases = (
        (5, True),
        (3, False),
        (1, True),
        (8, True),
        (41, True),
        (9, True),
        (4, True)
    )
    for arg, out in test_cases:
        result = sol.judgeSquareSum(arg)
        print(arg, result, out)
        assert result == out
