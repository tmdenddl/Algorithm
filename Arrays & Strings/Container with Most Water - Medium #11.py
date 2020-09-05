"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai)
For example: a1 = 5, then (1, 5) since i = 1 and a1 = 5 

n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0)

Find two lines, which together with x-axis forms a container, such that the container contains the most water

Real question:
Find the maximum difference between x position multiplied by the height
"""

def maxArea(self, height: List[int]) -> int:
    # Initialize variables
    maxArea = 0
    left = 0
    right = len(height) - 1

    while (left < right):
        # Note that water capacity can be calculated using the smaller building height
        # since water can only be contained up to shorter side
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
        
        # If height of the left building is smaller than the height of the right building,
        # move on to the left + 1 building
        # If not, move on to the right - 1 building
        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1


    return maxArea








"""
Time Complexity : O(n)
Space Complexity: O(1)
"""