"""
Two Sum - Easy #001

Given an array of integers and an integer target,
return indicies of 2 numbers in the array that add up to the target number

Example:

Input:
 - nums: [3, 6, 12, 14]
 - target: 15
Output: [0, 2]
"""

class Solution:
    def twoSums(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(n):
            # target - current value = goal
            goal = target - nums[i]
            # if goal is in map, 
            # return current index and index of the goal
            if (goal in m):
                return (m[goal], i)
            # if goal is NOT in the map,
            # add the current element and index to the map
            m[nums[i]] = i
        

        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""