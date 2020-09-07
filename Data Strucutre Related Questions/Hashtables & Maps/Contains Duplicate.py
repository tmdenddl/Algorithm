"""
Contains Duplicate - Easy #217

Given an array of integers, find if the array contains any duplicates
Return True if any value appears at least twice in the array, otherwise False

Example:

Input: [1, 2, 3, 1]
Output: True
"""
from Collections import defaultdict

class Solution:
    def twoSums(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        for num in nums:
            if (m[num]):
                return True
            m[num] += 1
        return False
        
        

        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""