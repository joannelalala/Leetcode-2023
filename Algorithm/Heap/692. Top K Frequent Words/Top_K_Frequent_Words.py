# min heap
# T: O(NlongK)
# M: O(N)

class Node(object):
    def __init__(self, freq, val):
        self.freq = freq
        self.val = val
        
    def __lt__(self, other):
        if self.freq < other.freq:
            return True
            
        if self.freq == other.freq:
            return self.val > other.val
            
class Solution:
    def topKFrequent(self, words: List[str], k :int) -> List[str]:
        counts = collections.Counter(words)
        heap = []
        i = 0
        for word, count in counts.items():
            if i < k:
                heapq.heappush(heap, Node(count, word))
            elif i >= k and heap[0] < Node(count, word):
                heapq.heappop(heap)
                heapq.heappush(heap, Node(count, word))
            i += 1
        return reversed([heapq.heappop(heap).val for x in range(k)])
        
# Link: https://leetcode.com/problems/top-k-frequent-words/
        
