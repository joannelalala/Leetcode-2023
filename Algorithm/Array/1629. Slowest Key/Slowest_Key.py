class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        largest_duration = 0
        start_time = 0
        result = ''
        for i, release_time in enumerate(releaseTimes):
            duration = release_time - start_time
            
            if duration > largest_duration:
                largest_duration = duration
                result = keysPressed[i]
                
            if duration == largest_duration:
                current_char = keysPressed[i]
                if ord(current_char) > ord(result):
                    result = current_char
                    
            start_time = release_time          
        return result
      
# TC: O(N)
# SC: O(1)
# Link: https://leetcode.com/problems/slowest-key/
                
        
