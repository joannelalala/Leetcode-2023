# Referred to : https://youtu.be/5Hie-4QPNtI

class Solution:
    
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # get the median first
        
        arr.sort()
        M = (len(arr)-1)//2
        
        median = arr[M]
        
        arr.sort(key = lambda x:(-abs(x-median), -x))
        
        return arr[:k]
        
        
