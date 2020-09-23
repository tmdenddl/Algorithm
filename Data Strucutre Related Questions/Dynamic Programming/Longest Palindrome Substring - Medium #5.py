"""
Longest Palindrome Substring - Medium #005

Given a string s, find the longest palindromic substring in s

Method:
- Create a matrix of size n * n where n is the number of characters in s
- i represents the columns and j represents the rows
- Each spot is a boolean value: True if s[i to j] is palindrome
- Since single characters are always palindrome, m[i][j] = True
- If the i-th index (which should be the start index) is bigger than j (last index), that range is false

Check if current substirng is padlindrome by checking if it's inner substring is palindrome and 
first and last characters of it are the same

How to check for inner substring?
- dp[i+1][j-1] or j - i <= 2

>> j - i <= 2 is for the cases if inner palindrome are empty string, single string which are always palindrome
>> dp[i+1][j-1] value will tell us if the inner palindrome from s[i+1] to s[j-1] is palindrome 

Example:

Input: 
babad 

Output:
bab
 

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if (n < 2):
            return s
        
        left = 0
        right = 0

        palindrome = [[0] * n for _ in range(n)]

        for j in range(1, n):
            for i in range(0, j):
                innerIsPalindrome = palindrome[i+1][j-1] or (j - i <= 2)
                
                if (s[i] == s[j] and innerIsPalindrome):
                    palindrome[i][j] = True
                    
                    if (j - i > right - left):
                        left = i
                        right = j

        return s[left:right+1]
        
"""
Time Complexity : O(N^2)
Space Complexity: O(N^2)
"""