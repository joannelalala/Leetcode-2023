'''
referred to https://youtu.be/aK-wqA8_G90

'''

class Solution:

    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        m = [[False]*n for _ in range(n)]
        
        for u, v in prerequisites:
            m[u][v] = True
        
        # Warshall's algorithm
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    m[i][j] |= m[i][k] and m[k][j]
                    
        ans = []
        
        for u, v in queries:
            ans.append(m[u][v])
            
        return ans
    
