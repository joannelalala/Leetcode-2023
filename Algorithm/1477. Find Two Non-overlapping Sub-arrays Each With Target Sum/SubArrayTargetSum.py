# referred to https://youtu.be/K_H-CyXnGF4

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        events = []
        N = len(arr)
        track = [1e100]*N
        current = 0
        mn = 1e100
        ans = 1e100
        
        left = right = 0
        while right < N:
        
            current += arr[right]
            right += 1
            
            while current > target:
            
                current -= arr[left]
                mn = min(track[left], mn)
                left += 1
                
            if current == target:
                track[right-1] = min(track[right-1], right -left)
                ans = min(ans, mn + right - left)
                    
        if ans >= 1e100:
            return -1 
        return ans
    

   
