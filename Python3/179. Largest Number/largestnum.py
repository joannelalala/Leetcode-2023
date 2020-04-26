class Node(str):
    def __lt__(a,b):
        return int(a+b) > int(b+a)
    
class Solution:    
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(map(Node, map(str, nums))))))
        
       
