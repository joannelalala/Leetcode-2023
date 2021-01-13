class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # create a dict
        
        for i, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = i
            else:
                return [d[n], i]
                
## Link: https://leetcode.com/problems/two-sum/
                
                
        
        
        
