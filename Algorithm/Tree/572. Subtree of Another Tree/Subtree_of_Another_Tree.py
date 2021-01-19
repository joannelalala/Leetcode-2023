# recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # check if the two subtrees are the same or not
        def check_is_same(s, t):
            if s is None and t is None:
                return True
            elif s is None or t is None:
                return False
            elif s.val != t.val:
                return False
            return check_is_same(s.left, t.left) and check_is_same(s.right, t.right)
        
        if s is None:
            return False
        # if equal
        if s.val == t.val and check_is_same(s, t):
            return True
            
        # otherwise, recurse in the left and right subtrees of s
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        
        return left or right
        
 # TC: O(|s||t|)
 # SC: O(s): the number of nodes in s
        
