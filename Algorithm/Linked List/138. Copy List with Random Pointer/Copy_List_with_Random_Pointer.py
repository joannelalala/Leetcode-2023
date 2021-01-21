# Recursive
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    '''
    :type head: Node
    :rtype: Node
    '''
    def __init__(self):
        # Dict which old nodes as its key and new nodes as its value
        self.visitedHash{}
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
            
        # if we have processed it, simply return the cloned version of it
        if head in visitedHash:
            return self.visitedHash[head]
            
        # create a new node with the value same as the old one
        node = Node(head.val, None, None)
        
        # save this value in the hashmap. This can avoid loops during traversal due to randomness
        self.visitedHash[head] = node
        
        # Recursively copy the remaining linked list starting once from the next pointer, then from the random pointer,
        # Thus, we have two indep. recursive calls
        # Finally, we update the next pointer and the random pointer for the new nodes created
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        
# TC: O(N)
# SC: O(N)
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/
        
