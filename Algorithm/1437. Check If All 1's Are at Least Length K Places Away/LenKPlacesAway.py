'''
referred to https://youtu.be/GsqMSazbYMs
'''

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        r = []
        
        for index, num in enumerate(nums):
            if num == 1:
                r.append(index)
                
        for a, b in zip(r, r[1:]):
            if b - a <= k:
                return False
        return True
    
