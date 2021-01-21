# Depth First Search with Hashset
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # helper function to do dfs
        
        def dfs(M, i):
            for j in range(len(M)):
                # if there is 1 in the corresponding matrix entry, and if the node is not visited
                if M[i][j] == 1 and j not in visited:
                    visited.add(j) # add to the visit set
                    dfs(M, j)
                    
       # length of node
        n = len(isConnected)
       
       # to track visited node
        visited = set()
       
       # count for connected components
        count = 0
       
       # up to the length of the node
        for i in range(0, n):
           # if the node not in visited set
            if i not in visited:
               # we start dfs on that node to explore
                dfs(isConnected, i)
               
               # for every new starting node, we increment one
                count += 1
               
        return count
  
# DFS with Hashset
# TC: O(N^2)
# SC: O(N)
# Link: https://leetcode.com/problems/number-of-provinces/
       
                    
