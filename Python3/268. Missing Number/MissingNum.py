class Solution:
    def missingNumber(self, nums)-> int:
        """
        :type: nums int List[int]
        :rtype: int
        """
        n=len(nums)
        result = n*(n+1)/2 - sum(nums)
        return int(result)
    
if __name__ == "__main__":
    nums = [3,0,1]
    print(Solution().missingNumber(nums))
