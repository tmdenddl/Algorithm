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

class Solution:
    def backtracking(self, ans, m, digits, combination, index):
        if (index > len(digits)):
            return

        if (len(combination) == len(digits)):
            ans.append(combination[:])
            return

        currentDigit = digits[index]
        currentString = m[currentDigit]

        for i in range(len(currentString)):
            self.backtracking(ans, m, digits, combination + currentString[i], index + 1)

    def letterCombination(self, digits: str) -> List[str]:
        ans = []
        if (len(digits) == 0):
            return ans
        
        m = {}

        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtracking(ans, m, digits, "", 0)

        return ans
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""