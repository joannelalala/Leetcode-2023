class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable={} # create a hash table
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
                break
            hashtable[num]=i
        return []
