"""
https://leetcode.com/problems/non-decreasing-array/

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution:
    @staticmethod
    def ever_decreases(li):
        last = li[0]
        for i in li[1:]:
            if i < last:
                return True
            last = i
        return False

    @staticmethod
    def decreases_consecutively(li):
        dec_counter = 0
        last = li[0]
        for i in li[1:]:
            if i < last:
                dec_counter += 1
            else:
                dec_counter = 0
            if dec_counter > 1:
                return True
            last = i
        return False

    def checkPossibility(self, nums):
        if not self.ever_decreases(nums):
            return True
        if self.decreases_consecutively(nums):
            return False
        for i, __ in enumerate(nums):
            li = list(nums)
            li.pop(i)
            if not self.ever_decreases(li):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        [4, 2, 3],
        [4, 2, 1])
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.checkPossibility(case)))
