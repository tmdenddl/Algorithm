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

class Solution:
    def solution(self, candidates, ans, cur, target, index, sum):
        if (sum == target):
            ans.append(cur[:])
        elif (sum < target):
            for i in range (index, len(candidates)):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, sum + candidates[i])
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