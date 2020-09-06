"""
Missing Number - Easy #268

Find the number that is missing from the array

Example:

Input: [3, 0, 1]
Output: 2

Explanation: From 0 ~ 3, we are missing 2

Algorithm used: Gauss Formula
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Sum of consecutive numbers = n(n+1)/2
        where n = biggest number = array length
        """
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = n*(n+1)/2

        return int(intendedSum - currentSum)


"""
Time Complexity : O(n)
Space Complexity: O(1)
"""