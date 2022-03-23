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

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buyPrice should be set to maximum value initially
        buyPrice = float("inf")
        profit = 0

        # Iterate over prices array with index 'i' and element 'price'
        for i, price in enumerate(prices):
            # If the current price is smaller than the buyPrice,
            # we should buy at the current price
            if (buyPrice > price):
                buyPrice = price
            # If the current price is smaller than the buyPrice,
            # we can sell the stock to gain profit.
            # Here we can compare the current profit with the maximum profit that was found so far.
            else:
                profit = max(profit, price - buyPrice)

        return profit

        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""