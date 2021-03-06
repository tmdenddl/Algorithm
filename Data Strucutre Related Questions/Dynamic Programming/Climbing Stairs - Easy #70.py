"""
Climbing Stairs - Easy #070

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: dp[i] = dp[i - 1] + dp[i -2]

Example:

Input: 
N = 6

Output:
 

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1

        dp = [0] * (n + 1)
        # 0 1 2 3 4
        # 0 1 2 3 4 5 

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i -2]

        return dp[n]

        
"""
Time Complexity : O(N)
Space Complexity: O(N)
"""