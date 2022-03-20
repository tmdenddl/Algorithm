"""
Letter Combination of Phone NUmber - Medium #017

Given a string containing digits from 2 to 9,
return all possible letter combinations that the number could present

Note: Think of an old phone
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz

Example:

Input: "23"
Output: [ "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""

from typing import List

class Solution:
    # ans = answer array
    # m = map between digits and corresponding letters
    # digits = current digit we're working on
    # combination = current combination string
    # index = current index we're on in the digits string
    def backtracking(self, ans, m, digits, combination, index):
        # This is an invalid case that we need to skip
        # We're out of bounds, so simply return to the previous recursive call stack
        if (index > len(digits)):
            return
        
        # If the combination string size is equal to the digits size
        if (len(combination) == len(digits)):
            # Add the current combination to the answer List
            # and return from the current recursive call
            ans.append(combination[:])
            return

        # Find the current digit
        # Find the corresponding characters for the current digit
        currentDigit = digits[index]
        currentString = m[currentDigit]

        # Loop over the currentString
        for i in range(len(currentString)):
            # Call the backtracking function but add 1 to the index, 
            # as well as adding the current character of the currentString to our combination
            self.backtracking(ans, m, digits, combination + currentString[i], index + 1)

    def letterCombination(self, digits: str) -> List[str]:
        ans = []

        # If we have an empty string, simply return empty List
        if (len(digits) == 0):
            return ans

        # Create a map between digits and corresponding letters
        m = {}
        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        # Call the recursive backtracking function
        self.backtracking(ans, m, digits, "", 0)

        return ans
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""