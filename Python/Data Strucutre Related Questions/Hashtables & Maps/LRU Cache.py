"""
LRU Cache - Medium #146

Design and implement a data structure for Least Recently Used (LRU) Cache
Given the capacity of the cache, implement a put and a get operation for an LRU cache

It should support the get and put operations

get(key): Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1
put(key, value): Set or insert the value if the key is not already present

When the cache reachced its capacity, put(key, value) should invalidate the least recently used item before inserting a new item

Example:

Input:
Cache: [2, 3, 4, 5]

Note: This order means that 2 was accessed the most recently, followed by 3, 4 then 5

Output: 

"""

from collections import deque

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = dict()
        self.deq = deque()
    
    def get(self, key: int) -> int:
        # If there is key in the map, move it to the front of the queue
        # In other words, add the key as most recently used
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1
    
    def put(self, key:int, value: int) -> None:
        # If there is not key in the map,
        if key not in self.m:
            # If the capacity is full
            if len(self.deq) == self.capacity:
                # delete the oldest key from the queue and map
                oldest = self.deq.popleft()
                del self.m[oldest]
        # If there is key in the map, remove the key from the queue
        else:
            self.deq.remove(key)

        # Add the key to the map and add it to the queue as most recently used
        self.m[key] = value
        self.deq.append(key)
        
"""
Time Complexity : O(1)
Space Complexity: O(n)
"""  

s = LRUCache(3)
s.put(1, 1000)
s.put(2, 2000)
s.put(3, 3000)

# [1, 2, 3]

print(s.get(1)) # 1000

# [2, 3, 1]

s.put(4, 4000)

# [3, 1, 4]  Note: 2, which is the least recently used, is removed

print(s.get(2)) # -1
print(s.get(3)) # 3000

# [1, 4, 3]