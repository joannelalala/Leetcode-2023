# sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # firstly, sort the input
        intervals.sort(key= lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty, or the previous does not overlap with the current, just append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                
            else:
                # there is overlap, we merge
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged    
        
# TC: O(nlongn)
# SC: O(n)
# Link: https://leetcode.com/problems/merge-intervals/
