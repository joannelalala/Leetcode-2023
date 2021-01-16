# categorize by sorted string: TC:O(NKlongK), sort takes O(KlogK), N is the length of strs, SC:O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # categorize by sorted string
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        
# categorize by count TC: O(NK), SC: O(NK), N is the length of strs, and K is the maximum length of a string in strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # categorize by count
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            ans[tuple(count)].append(s)
            
        return ans.values()
        
        
# Link: https://leetcode.com/problems/group-anagrams/
