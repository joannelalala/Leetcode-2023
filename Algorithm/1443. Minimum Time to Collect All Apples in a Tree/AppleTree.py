'''
referred to https://blog.csdn.net/zjucor/article/details/106088181

'''

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        from collections import defaultdict
        adj = defaultdict(list)
        for s,t in edges:
            adj[s].append(t)
            adj[t].append(s)
 
        tree = defaultdict(list)
        vis = set([0])
        q = [0]
        while q:
            s = q.pop()
            for t in adj[s]:
                if t in vis: continue
                tree[s].append(t)
                vis.add(t)
                q.append(t)
 
        # memo = {}
        def helper(s):
            if s not in tree:
                return 0,hasApple[s]
            res = 0
            tt = [helper(t) for t in tree[s]]
            for su,flag in tt:
                if flag:
                    res += su+2
            # memo[s] = (res, any(t[1] for t in tt) or hasApple[s])
            return res, any(t[1] for t in tt) or hasApple[s]
 
        # helper(0)
        return helper(0)[0]
        
        

