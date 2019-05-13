"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

import statistics


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return float(statistics.median(nums1 + nums2))


def main():
    sol = Solution()
    test_cases = [[[1, 3], [2]], [[1, 2], [3, 4]]]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.findMedianSortedArrays(*case)))


if __name__ == '__main__':
    main()
