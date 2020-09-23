"""
House Robber - Easy #198

Say you are a house robber who can't rob two adjacent house.
You are given a list of non-negative integers representing the amount of money in each house,
find the maximum amount you can steal


Example:

Input: 
[1, 2, 3, 1]

Output:
4

"""

class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if (i == 1):
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
        
"""
Time Complexity : O(N)
Space Complexity: O(N)
"""