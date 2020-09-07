"""
Majority Element - Easy #169

Given an array of integers of size N, find the majority element of the array
A majority element appears more than n/2 times where n is the array size

Example:

Input: [1, 2, 3, 1, 1]
Output: 1
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            # Increment num counter in the map
            # If adding for the first time, consider the counter as 0
            m[num] = m.get(num, 0) + 1

        for num in nums:
            # If there is an element that takes at least half of the array, return the element
            if(m[num]>len(nums)//2):
                return num
        # If no majority element is found
        return -1
        

        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""