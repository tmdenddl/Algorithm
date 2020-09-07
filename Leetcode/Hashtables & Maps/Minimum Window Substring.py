"""
Minimum Window Substring - Hard #076

Given a string S and a string P, find the minimum window in S which will contain all the characters in P

Example:

Input:
S: "ADOBECODEBANC"
P: "ABC"

What is the smallest substring that contains the letters A, B, C?

Output: "BANC"

"""

from collections import deque

class Solution:
    def minWindow(self, s: str, p:str) -> str:
        lengthString = len(s)
        lengthPattern = len(p)

        # If the given pattern has more characters than the given string,
        # there would be no minimum window, thus return empty string
        if (lengthString < lengthPattern):
            return ""

        # Initialize two dictionaries for String S and Pattern P
        hashString = {}
        hashPattern = {}
        
        # Loop over the Pattern
        for i in range(0, lengthPattern):
            # If the current character is not in hashPattern,
            # initialize its key in the hashMap
            if (hashPattern.get(p[i]) is None):
                hashPattern[p[i]] = 0
            # If the character already exist in the hashPattern,
            # increment its value by 1
            hashPattern[p[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minimumLength = float("inf")

        # Loop over the String
        for right in range(0, lengthString):
            # If the current character is not in hashString,
            # initialize its key in the hashMap
            if (hashString.get(s[right]) is None):
                hashString[s[right]] = 0
            # If the current character is in the hashString,
            # increment its value by 1
            hashString[s[right]] += 1

            # If the current character is not in hashPattern,
            # initialize its key in the hashMap
            if (hashPattern.get(s[right]) is None):
                hashPattern[s[right]] = 0

            # If the window has not yet covered the number of occurence of the current character in P
            # increment the counter
            if (hashString.get(s[right]) <= hashPattern.get(s[right])):
                count += 1

            # Window contains all the charcters in P
            if (count == lengthPattern):
                # Move the left pointer to the right only if we still have more occurence of the characters than needed after moving the pointers
                while (hashString.get(s[left]) > hashPattern.get(s[left])):
                    hashString[s[left]] -= 1
                    left += 1
            
                # If the current window size is smaller than the smallest window size so far,
                # minimumLength now equals to current window size and
                # startIndex should point to left of the current window
                windowLength = right - left + 1
                if (minimumLength > windowLength):
                    minimumLength = windowLength
                    startIndex = left

            if (startIndex == -1):
                return ""
            
            windowSize = startIndex + minimumLength
            return s[startIndex:windowSize]


        
"""
Time Complexity : O(|S| + |P|)
Space Complexity: O(|S| + |P|)
"""