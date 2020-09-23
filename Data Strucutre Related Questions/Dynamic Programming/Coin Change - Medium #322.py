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

class Solution:
    def coinChange(self, coins: Lis[int], amount: int) -> int:
        if (amount <= 0):
            return 0
        
        if (min(coins) > amount):
            return -1
        
        INT_MAX = 1 << 32
        dp = [INT_MAX] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] != INT_MAX else -1
        
"""
Time Complexity : O()
Space Complexity: O()
"""