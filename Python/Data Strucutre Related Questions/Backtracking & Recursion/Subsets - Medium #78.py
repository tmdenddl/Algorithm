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

class Solution:
    def solution(self, nums, ans, cur, index):
        if (index > len(nums)):
            return
        ans.append(cur[:])
        for i in range (index, len(nums)):
            if (nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums, ans, cur, i)
                cur.pop()
        return

    def subsets(self, num: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans
    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""