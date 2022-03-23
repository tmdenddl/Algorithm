"""
Unique Paths - Medium #060

You are given a m*n grid with a robot located at the top left corner (0, 0).
The robot is trying to reach the bottom-right corner (m - 1, n - 1) of the grid.
The robot can ONLY move either down or right at any point in time.
How many possible unique paths are there to reach that final cell?

Note: 
- Since we can only move either down or right, we can reach first row/column in only 1 way
- The number of ways to reach some position, i, is equal to 
    the number of ways we reached the position above + the number of ways we reached the element on it's left

Example:

Input: 
[
    [R, *, *],
    [*, *, *],
    [*, *, Goal]
]

Output:

 

"""

class Solution:
    def uniquePath(self, m: int, n: int) -> int:
        # Created a matrix of size m * n
        dp = [[0 for x in range(m)] for y in range(n)]

        # For any positions on the first row, we ONLY have 1 way to reach it
        for i in range(m):
            dp[0][i] = 1

        # Likewise, for any positions on the first column, we ONLY have 1 way to reach it
        for i in range(n):
            dp[i][0] = 1

        # For any other positions in the grid
        for i in range(1, n):
            for j in range(1, m):
                # As we can only move DOWN or RIGHT, we can reach the position from it's above or left.
                # Therefore, the # of ways to reach the current position dp[i][j] is 
                # sum of the # of ways to reach the position above or left of the current position.
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Return the solution at the bottom-right corner
        return dp[-1][-1]
        
"""
Time Complexity : O(N*M)
Space Complexity: O(N*M)
Where N is the number of Columns and M is the number of rows
"""