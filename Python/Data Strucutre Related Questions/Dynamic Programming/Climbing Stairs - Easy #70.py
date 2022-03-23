"""
Climbing Stairs - Easy #070

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: dp[i] = dp[i - 1] + dp[i -2]

Breakdown:
- How many ways can we climb to step 1?


Example:

Input: 
N = 6

Output: 13
 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # If there's only 1 step, we only have 1 way to climb it
        if (n == 1):
            return 1

        # Initialize an array to store solutions of the dynamic programming
        # Note we'll begin the array from index 1
        dp = [0] * (n + 1)
        # 0 1 2 3 4
        # 0 1 2 3 4 5 

        # The first step can be reached in only 1 way
        # Likewise, the second step can be reached in only 2 ways
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            # The # of ways to reach step i equals to:
            # the # of ways that we can reach step (i - 1) + the # of ways that we can reach step (i - 2)
            dp[i] = dp[i - 1] + dp[i -2]

        return dp[n]

        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""

s = Solution()
ans = s.climbStairs(6)
print(ans)