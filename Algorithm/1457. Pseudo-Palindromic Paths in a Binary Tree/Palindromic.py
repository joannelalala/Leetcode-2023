# referred to https://youtu.be/LiQGJ16m5Rw

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = 0
        
        def go(node, current):
            nonlocal ans
            
            if node is None:
                return
        
            current ^= (1<< node.val)
        
            if node.left is None and node.right is None:
                count = 0
                for i in range(10): # Node values are digits from 1 to 9
                    if ((current >> i)& 1) > 0:
                        count +=1    
                if count <= 1:
                    ans+=1
                
            go(node.left, current)
            go(node.right, current)
        
    
        go(root, 0)
        return ans
