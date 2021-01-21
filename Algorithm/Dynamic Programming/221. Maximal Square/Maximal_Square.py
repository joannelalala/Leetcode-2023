class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming: bottom-up
        # recursively: top-down
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # create a cache, which is the hashmap in Python
        cache = {}
        
        # create a helper function
        
        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
                
            if (r, c) not in cache:
                # compute the maxarea
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                
                cache[(r, c)] = 0
                if matrix[r][c] == '1': # here the o and 1 in the matrix are string
                    cache[(r, c)] = 1 + min(down, right, diag)
                    
            return cache[(r, c)]
            
       # call the helper function
       helper(0,0) 
       return max(cache.values()) ** 2
       
 # For recursive sol, 
 # T: O(M*N), which M stands for the width of the matrix, and N stands for the height of the matrix
 # M: O(M*N)
 # For dynamic programming, the M can be reduced, but the recursive sol is easier for me to understand
 
 # Link: https://leetcode.com/problems/maximal-square/
