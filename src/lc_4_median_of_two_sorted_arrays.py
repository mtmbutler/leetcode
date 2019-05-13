"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n
respectively.

Find the median of the two sorted arrays. The overall run time
complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        total_len = len(nums1) + len(nums2)
        half_len = total_len / 2
        even = total_len % 2 == 0

        # Start merging but stop when we get to the middle
        li = []  # Final list
        i = 0  # nums1 index
        j = 0  # nums2 index
        while True:
            # Check exit condition
            merged = i + j
            if even and merged == half_len + 1:
                return sum(li[-2:]) / 2  # Average middle 2 elements
            elif not even and merged > half_len:
                return li[-1]

            # Keep merging
            nums1_spent = i >= len(nums1)
            nums2_spent = j >= len(nums2)
            if not nums1_spent and (nums2_spent or nums1[i] <= nums2[j]):
                li.append(nums1[i])
                i += 1
            elif not nums2_spent:
                li.append(nums2[j])
                j += 1
            else:
                return li[-1]


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        ([[1, 3], [2]], 2),
        ([[1, 2], [3, 4]], 2.5),
        ([[], [1]], 1),
        ([[1], []], 1))
    for args, out in test_cases:
        result = sol.findMedianSortedArrays(*args)
        assert result == out
