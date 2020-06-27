'''
referred to https://youtu.be/p0G_e5O22Fo
'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
    
    # classic sliding window problem
        
        current = 0
        mask = (1 << k) -1
        a = set()
        
        for index, x in enumerate(s):
            current <<= 1
            current += int(x)
            current &= mask
            
            if index >= k -1:
                a.add(current)
                
        return len(a) == (1 << k)
    
    
