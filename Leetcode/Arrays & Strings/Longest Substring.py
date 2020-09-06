"""
Longest Substring - Medium #003

Longest Substring without Repeating Characters

Given a string, find the length of the longest substring without repeating characters
"""
class Solution:
    def longestSubstring(self, string: str) -> int:
        map = {}
        # left = start of the substring
        # right = current position of the substring
        # ans = longest length of the substring so far
        left, right, ans = 0
        n = len(string)

        # loop until reaching the end
        while (left < n and right < n):
            # Set elemnt to current character in the string
            element = string[right]
            
            # If the element is already in the map
            if (element in map):
                # Set the add 1 to the current start of the substring
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