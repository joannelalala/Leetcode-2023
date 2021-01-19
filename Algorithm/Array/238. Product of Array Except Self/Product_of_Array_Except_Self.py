class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
            
        # for the element at length - 1, there are no elements to the right of it, so R would be 1    
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
        
# TC: O(N)
# SC: O(1)

# Link: https://leetcode.com/problems/product-of-array-except-self/
