"""
Coin Change - Medium #322

You are given coins of different values and a total amount of money.
Write a function to compute the fewest number of coins that you need to make up that amount.
If amount can't be made, return -1

Example:

Input: 
Coins = [1, 2, 5]
Amount = 11

Output:
3 coins (5 + 5 + 1 = 11)
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If the amount is less or equal to 0, we have no solution...
        if (amount <= 0):
            return 0
        
        # If the amount can't be made, return -1
        if (min(coins) > amount):
            return -1
        
        # Initialize DP table, each index filled with the maximum number
        # Note that we're starting at index 1
        INT_MAX = 1 << 32
        dp = [INT_MAX] * (amount + 1)

        # Same logic as the base case, we can't make up amount 0 with coins...
        dp[0] = 0

        # Loop until we reach the given amount in DP solutions
        for i in range(1, amount + 1):
            # For the possible coins we can use...
            for coin in coins:
                # If the coin is smaller or equal to the current amount, our solution for the sub-problem is still valid
                # The minimum # of coins required to reach i would be the minimum of:
                # # of coins requierd to reach (i - coin) + 1 as we only need extra coin (current coin)
                # or the current minimum # of coins required for the amount i (This could be calculated from the previous coins)
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        # Unless the minimum # of coins required to reach the amount is still INT_MAX, we've found the answer
        return dp[amount] if dp[amount] != INT_MAX else -1
        
"""
Time Complexity : O()
Space Complexity: O()
"""