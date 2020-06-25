'''
referred to https://youtu.be/Ok0jYAMnvQI
'''
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        
        N = len(favoriteCompanies)
        s = []
        for x in range(N):
            s.append(set(favoriteCompanies[x]))
            
            
        r = []
        
        for i in range(N):
            found = False
            
            for j in range(N):
                if found:
                    continue
                if i != j:
                    for k in s[i]:
                        if k not in s[j]:
                            break
                        
                    else:
                        found = True
                        
            if not found:
                r.append(i)
                
        return r
