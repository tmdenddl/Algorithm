"""
House Robber - Easy #198

Say you are a house robber who can't rob two adjacent house.
You are given a list of non-negative integers representing the amount of money in each house,
find the maximum amount you can steal

Tip:
- What is the maximum amount that you can steal up to i-th position?
- For the first house, we can only steal from the first house
- For the second house, we can either choose to steal from the first or the second house
- From third house onwards, we have different options:
    1. Don't take money from the current house. Then we can just keep the amount of money
       that we have stolen up to the previous position.
    2. Steal from current house. In this case, we can't steal from previous house.
       We need to add the amount to the maximum amount that could be stolen at (current - 2)th house.

Example:

Input: 
[1, 2, 3, 1]

Output:
4
"""

from typing import List

class Solution:
    def houseRobber(self, nums: List[int]) -> int:
        n = len(nums)

        # We can't really steal anything if the list is empty
        if (n == 0):
            return 0

        # Initialize the array to store the previous answers of DP problem,
        # and store the first element at the inex 0 since it's the only possible answer
        dp = [0] * n
        dp[0] = nums[0]
        
        # Loop through the list
        for i in range(1, n):
            # If we're at index 1, we simply choose the greater of element at index 0 or index 1
            if (i == 1):
                dp[i] = max(nums[0], nums[1])
            # Otherwise, we need to compare if the previous solution is greater, or the new solution is greater
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # Return the maximum amount at the last of the array which would contain the final solution
        return dp[-1]
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""