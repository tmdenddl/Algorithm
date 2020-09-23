"""
Best Time to Buy and Sell Stock - Easy #121

Given an array of integers where each element value at a position i represent the price of stock at day i,
design an algorithm to find the maximum profit given that you're allowed only one transaction

Analysis: position of the maximum element must be AFTER position of the minimum element
    - We actually want to find the maximum (x - y) where x comes after y in the array


Example:

Input: 
[7, 1, 5, 3, 6, 4]

Output:
5

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0

        for i, price in enumerate(prices):
            if (buyPrice > price):
                buyPrice = price
            else:
                profit = max(profit, price - buyPrice)

        return profit

        
"""
Time Complexity : O(N)
Space Complexity: O(1)
"""