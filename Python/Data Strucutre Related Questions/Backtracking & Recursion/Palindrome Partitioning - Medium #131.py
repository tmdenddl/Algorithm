"""
Palindrome Partitioning - Medium #131

Given a string S, partition S such that every substring of the partition is a palindrome,
return all possible palindrome partitioning of S

Palindrome is a string that can be read the same in a reverse order.

Example:

Input: "aab"

Output:
[
    ["aa", "b"],
    ["a", "a", "b"]
]

"""

from typing import List

class Solution:
    def isPalindrome(self, seg):
        i = 0
        j = len(seg) - 1

        # A string is a palindrome if the all nth character from the start and from the end of the string are the same
        while (i < j):
            if (seg[i] != seg[j]):
                return False
            i += 1
            j -= 1
        
        return True


    def dfs(self, s: str):
        # If the string is empty, our traversal of the string has reached the end
        if (len(s) == 0 and len(self.temp) > 0):
            # Append the partitioned substrings to the result array
            self.res.append(self.temp[:])
            return
        
        # Loop over the length of the string
        n = len(s) + 1
        for i in range(1, n):
            # Get a segment that starts from index 0 to the index i
            seg = s[0:i]
            # If the segment is a palindrome
            if (self.isPalindrome(seg)):
                # Append the segment to the temporary array
                self.temp.append(seg)
                # Call a recursive backtracking function to check for the remaining characters in the string
                self.dfs(s[i:])
                # Discard the current segment in the call stack
                self.temp.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.temp = []
        self.dfs(s)

        return self.res
        
    
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""