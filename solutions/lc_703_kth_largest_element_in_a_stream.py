"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it
is the kth largest element in the sorted order, not the kth distinct
element.

Your KthLargest class will have a constructor which accepts an integer k
and an integer array nums, which contains initial elements from the
stream. For each call to the method KthLargest.add, return the element
representing the kth largest element in the stream.

Note:
 - You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
from typing import List


class KthLargest:
    """A collection that keeps track of its kth-largest member.

    Note that it doesn't actually remember the entire collection -- for
    performance, it only keeps the largest k elements.

    Example:
        >>> obj = KthLargest(k=3, nums=[4, 5, 8, 2])
        >>> obj.add(3)   # [2, 3, 4, 5, 8]
        4
        >>> obj.add(5)   # [2, 3, 4, 5, 5, 8]
        5
        >>> obj.add(10)  # [2, 3, 4, 5, 5, 8, 10]
        5
        >>> obj.add(9)   # [2, 3, 4, 5, 5, 8, 9, 10]
        8
        >>> obj.add(4)   # [2, 3, 4, 4, 5, 5, 8, 9, 10]
        8
    """
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]

    def add(self, val: int) -> int:
        if val <= self.nums[0]:
            return self.nums[0]
        else:
            self.nums = self.nums[1:]
            for i, n in enumerate(self.nums):
                if val < n:
                    self.nums.insert(i, val)
                    return self.nums[0]
            self.nums.append(val)
            return self.nums[0]
