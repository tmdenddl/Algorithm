"""
Move Zeros - Easy #283

Given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the other elements
"""

from typing import List

class Solution:
    def moveZeros(self, arr: List[int]) -> None:
        j = 0
        length = len(arr) - 1

        for num in arr:
            if (num != 0):
                arr[j] = num
                j += 1

        for i in range(j, length):
            arr[i] = 0
        print(arr)    

    """
    Time Complexity : O(n + m)
    Space Complexity: O(1)
    """

s = Solution()
s.moveZeros([0, 2, 0, 1, 4]) # Expected output: [2, 1, 4, 0, 0]