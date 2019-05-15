"""
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU)
cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already
present. When the cache reached its capacity, it should invalidate the
least recently used item before inserting a new item.

Follow up:

Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        # The key/value pairs are stored in a simple ordered dict.
        # The dict is ordered from left to right by usage, with the
        # least recently used on the left.
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        val = self.d.pop(key, -1)
        if val != -1:
            self.d[key] = val  # Re-add the value to the right end
        return val

    def put(self, key, value):
        existing_val = self.d.pop(key, -1)
        if existing_val == -1 and len(self.d) == self.capacity:
            # Pop the least-recently-used value
            self.d.popitem(last=False)
        self.d[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    # Test 1
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Test 2
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(1, 1)
    cache.put(4, 1)  # evicts key 2
    assert cache.get(2) == -1
