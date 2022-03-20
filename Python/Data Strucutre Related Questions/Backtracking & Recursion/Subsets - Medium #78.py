"""
Subsets - Medium #078

Given a set of distinct integers, nums, return all possible subsets

Note: 
- The solution set must not contain duplicate subsets
    e.g. We can't have [1, 2] and [2, 1]
- Number of possible subsets is: 2 ^ n

Example:

Input: [1, 2, 3]
Output: 
[
    [],
    [1], [2], [3]
    [1, 2], [1, 3], [2, 3],
    [1, 2, 3]
]
"""

from typing import List

class Solution:
    # nums = input array
    # ans = answer array
    # cur = current subset we're on
    # index = index of an element that we're currently working on
    def solution(self, nums, ans, cur, index):
        # If index is bigger than the length of the array, return
        if (index > len(nums)):
            return

        # Append the current array into answer array
        ans.append(cur[:])

        # Loop from index to the end of the input array
        for i in range (index, len(nums)):
            # Check to see if the current element is not present in our current array
            # This is to prevent having duplicates
            if (nums[i] not in cur):
                # Append the current element into the current subset
                cur.append(nums[i])
                # Recursively call the solution method with updated current subnet
                self.solution(nums, ans, cur, i)
                cur.pop()
        return

    def subsets(self, num: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        # Call an external backtracking method that will contain our full logic
        self.solution(num, ans, cur, 0)
        return ans
    
"""
Time Complexity : O()
Space Complexity: O()
"""


