# OrderedDictionary

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        
        self.capacity = capacity
        
    def get(self, key: int):
        """
        :type key:int
        :rtype: int
        
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
        
    def put(self, key: int, value: int):
        """
        :type key:int
        :type value:int
        :rtype:void
        """
        
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capactiy:
            self.popitem(last = False)
            
# TC:O(1)
# SC:O(capacity)
# Link: https://leetcode.com/problems/lru-cache/
