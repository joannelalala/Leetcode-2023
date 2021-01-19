# stack
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop() # remove it from the record
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
         
# TC: O(N)
# SC: O(N)
# Link: https://leetcode.com/problems/baseball-game/
                
