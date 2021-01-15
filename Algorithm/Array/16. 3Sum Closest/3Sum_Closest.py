## Two Pointers
## if would like to achieve SC: O(1) can use selection sort in two pointers

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
        
            while(lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
                
            if diff == 0:
                break
            
        return target - diff

# TC: O(n^2)
# SC: O(longn) -> O(n), depending on the implementation of the sorting algorithm

# Link: https://leetcode.com/problems/3sum-closest/

                    
