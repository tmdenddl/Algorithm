"""
Combination Sum - Medium #039

Given a set of positive candidate numbers (without duplicates) and a target number,
find all unique combination of candidates where the candidates numbers sums to target

Note: The same repeated number may be chosen from candidates unlimited number of times
Note: The solution set must not contain duplicate combinations


Example:

Input:

candidates: [2, 3, 6, 7]
target: 7

Output:
[
    [7],
    [2, 2, 3]
]

"""

from typing import List

class Solution:
    # candidate = list of the candidate numbers
    # ans = list of the possible combinations that sums to target
    # cur = current combination of the numbers
    # target = a target number that the combination of the numbers should sum to
    # index = index to track of the current index within the candidates list 
    # sum = sum of the current combination of the numbers
    def solution(self, candidates, ans, cur, target, index, sum):
        # We stop the search in two cases:
        # 1. when we find a valid combination (sum === target)
        # 2. when our combination sum is bigger than our target (sum > target)

        # If we find a combination that's equal to the target, append the combination to the answer
        if (sum == target):
            ans.append(cur[:])
        # If the combination is smaller than our target, we still have chance of reaching the target
        elif (sum < target):
            # Try all the possible candidates using a loop
            for i in range (index, len(candidates)):
                # Append the current candidate to the current combination,
                # and check if the solution is found using backtracking recursive function
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, sum + candidates[i])
                # Remove the last added candidate, so we can try different candidates
                cur.pop()
        return


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates, ans, cur, target, 0, 0)

        return ans

"""
Time Complexity : O()
Space Complexity: O()
"""