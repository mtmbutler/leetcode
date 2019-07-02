"""
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of
length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k such that arr[i] < arr[j] < arr[k]
given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space
complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = None
        for n in nums:
            if a is None or n <= a:
                a = n
            elif b is None or n <= b:
                b = n
            else:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        [[1, 2, 3, 4, 5], True],
        [[5, 4, 3, 2, 1], False],
        [[5, 4, 1, 3, 5], True],
        [[5, 1, 2, 0, 2, 4], True],
        [[1, 4], False],
        [[1, 5, 10], True],
        [[], False],
        [[19], False],
        [[5, 1, 5, 5, 2, 5, 4], True],
        [[1, 1, 1, 1, 1, 1], False],
        [[5, 1, 5, 5, 0, 0, 0, 0, 8], True]
    )
    for arg, out in test_cases:
        result = sol.increasingTriplet(arg)
        print(arg, result, out)
        assert result == out
