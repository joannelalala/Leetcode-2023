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

# Iterative

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
        # create a dict to use old nodes as key and new nodes as values
        self.visited = {}
        
    def getClonedNode(self, node):
        # if node exists then
        if node:
            # check if it exists in the dict
            if node in self.visited:
                # return the new node reference from the dict
                return self.visited[node]
            else:
                # add the node to the dict
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
            return None
        
    def copyRandomList(self, head):
        '''
        :type head: Node
        :rtype: Node
        '''
        if not head:
            return head
        
        old_node = head
        
        # create a new head node
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        
        # iterate over the linked list until all nodes are cloned
        while old_node != None:
            # get the cloned of the nodes reference by next pointer and random pointer
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)
            
           # Move on step ahead in the linked list
           old_node = old_node.next
           new_node = new_node.next
        
        return self.visited[head]
    
# Iterative
# TC: O(N)
# SC: O(N)


       
        
        
        
        
