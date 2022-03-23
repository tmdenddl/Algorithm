"""
Trapping Rain Water- Hard #042

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining

Note: Water must be surrounded by 2 building on it's left and right, 
where at least one building have to be of height bigger than or equal to the water

Method:
- Since left[i] contain the maximum height between the tallest building on the left of the i-th building
or current height[i] itself, left[0] will always be equal to height[0]
- Loop over our input array from beginning to the end and update the tallest building on the left of current building i

- Since right[i] contains the maximum height between the tallest building on the right of i-th building
or current height (height[i]) itself, right[N - 1] will always be equal to height[N-1]
- Loop over our input array from end to beginning and update the tallest building on the right of the current building i

- Loop over our input array, increment the amount of water that we have using this formula:
    water += min(left[i], right[i]) - height[i]

Example:

Input: 
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output:
6
"""

from typing import List

class Solution:
    def trappingRain(self, height: List[int]) -> int:
        # Number of integers in the elevation map
        n = len(height)

        # If the height list is empty, we can't trap any water
        if (n == 0):
            return 0

        # Initialize left and right array for Dyanmic Programming
        # left array will contain the maximum height between the tallest building on the left of i-th building or height[i] itself
        # right array will contain the height between the tallest building on the right of i-th building or height[i] itself
        left = [0] * n
        right = [0] * n

        # Amount of water stored so far
        water = 0

        # Since left[i] contains the maximum height between the tallest building on the left of the i-th building
        # or current height[i] itself, left most index (left[0])  will always be equal to height[0]
        # In other words, there's no building on the left of 0 index, thus height at index 0 will be the maximum height found
        left[0] = height[0]

        # Since right[i] contains the maximum height between the tallest building on the right of the i-th building
        # or current height[i] itself, right most index (right[n-1]) will always be equal to height[n-1]
        # In other words, there's no building on the right of the last index (n-1), thus height at index n-1 will be the maximum height found
        right[n-1] = height[n-1]

        # Loop over the list, and store the maximum height between the tallest building that's on the left of current index found so far (left[i - 1]),
        # or the height at the current index (height[i])
        for i in range(1,n):
            left[i] = max(left[i-1], height[i])

        # Loop over the list, and store the maximum height between the tallest building that's on the right of current index found so far (right[i + 1]),
        # or the height at the current index (height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        # Now we've found the tallest buildings on the left and right of each index i,
        # calculate the toal amount of water that could be trapped
        # Note that the maximum water that could be trapped between the two indexes is the minimum height of those two indexes,
        # otherwise, the water would overflow
        for i in range(0, n):
            water += min(left[i], right[i]) - height[i]
        
        return water
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""