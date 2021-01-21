# Note that 1 does not map to any letters.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        :type: digits: str
        :rtype: List[str]
        '''
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'], 
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z'] 
        }
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
                
            # if there are still digits to check
            
            else:
                # iterate all letters which map the next available digits
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination and proceed to the next digit
                    backtrack(combination + letter, next_digits[1:])
        output = []
        if digits:
            backtrack("", digits)
          
        return output
      
  # recursion
  # TC: O(3^M*4^N), which M is the number of digits which maps to 3 letters, and M is the number of digits which maps to 4 letters, and M+N is the total number of digits in the 
  # inout
  # SC: O(3^N*4*M)
  # Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
  
                
