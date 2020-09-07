"""
Group Anagrams - Medium #049

Given an array of strings, group anagrams together
An anagram is a word formed by re-arranging the letters of a different word

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: 
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]
"""

class Solution:
    def findHash(self, s: str):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            # Sort the string
            hashed = self.findHash(s)
            # If hashed is not in the map, initialize one
            if (hashed not in m):
                m[hashed] = []
            # Append the string as value to the map where hashed value is the key
            m[hashed].append(s)

        for p in m.value():
            answers.append(p)

        return answers
        

        
"""
Time Complexity : O(n * m * log(m))
    - n: length of the input array
    - m: length of biggest string in the array
Space Complexity: O(n)
"""