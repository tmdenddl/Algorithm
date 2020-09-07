"""
Single Number - Easy #136

Given a non-empty array of integers, every element appears twice except for one, find it

Example:

Input: [2, 2, 1, 1, 4]
Output: 4

Explanation: 2*(1 + 2 + 4) - (1 + 1 + 2 + 2 + 4) = 4
    - 2 * (a + b + c) - (a + a + b + b + c) = c
    - (a + b + c)         => summation of the unique elements that you have
    - (a + a + b + b + c) => summation of all elements that you have

Algorithm used: 
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


"""
Time Complexity : O(n)
Space Complexity: O(n)
"""