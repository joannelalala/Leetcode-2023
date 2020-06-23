## referred to https://youtu.be/fPQZ-dZ8Wgc

class Solution:
    
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        # initialize count to 0
        
        count = 0
        
        adjList = collections.defaultdict(list)
        
        for u , v in connections:
            
            adjList[u].append([v,1])
            adjList[v].append([u,0])
            
        seen = set()
        
        def go(node):
            nonlocal count
            for x, direction in adjList[node]:
                if x not in seen:
                    count+=direction
                    seen.add(x)
                    go(x)

        seen.add(0)
        go(0)
            
        return count


