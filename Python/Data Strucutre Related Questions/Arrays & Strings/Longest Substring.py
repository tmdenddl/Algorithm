"""
Longest Substring - Medium #003

Longest Substring without Repeating Characters

Given a string, find the length of the longest substring without repeating characters
"""

class Solution:
    def longestSubstring(self, s: str) -> int:
        # Map to store the characters and the last index the character was found at
        # left = start of the substring
        # right = current position of the substring
        # ans = longest length of the substring so far
        map = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)

        # If the String is a single or empty String, return it's length
        if n <= 1:
            return n

        # loop until reaching the end
        while (left < n and right < n):
            # Set elemnt to current character in the string
            element = s[right]
            
            # If the element is already in the map
            if (element in map):
                # Set left to bigger index between current left and the next index of where the current element was foud last 
                left = max(left, map[element] + 1)
            # Set the character's new position
            map[element] = right
            # right - left + 1 is length of the substring
            ans = max(ans, right - left + 1)
            right += 1

        return ans

"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()
answer = s.longestSubstring("abcabcbd")

# sub | string
# Answer would be # of characters in the right subarray (string)
# Therefore the answer is 5
print(answer)
