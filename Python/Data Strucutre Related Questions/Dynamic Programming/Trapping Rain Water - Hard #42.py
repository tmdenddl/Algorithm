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

class Solution:
    def trappingRain(self, height: List[int]) -> int:
        n = len(height)

        if (n == 0):
            return 0

        left = [0] * n
        right = [0] * n

        water = 0

        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i-1], height[i])

        for i in range(0, n):
            water += min(left[i], right[i]) - height[i]
        
        return water
        
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""