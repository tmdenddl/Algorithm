"""
Robot Return to Origin - Easy #204

Imagine a robot standing at position (0,0) in a 2D grid,
given a string consisting of it's moves, find if the final location of the robot is at origin

U: Up       INCREASE in y axis
D: Down     DECREASE in y axis
R: Right    INCREASE in x axis
L: Left     DECREASE in x axis

Example:

Input: UD
Output: TRUE

Explanation:

U  => (0, 0+1) = (0, 1)
UD => (0, 1-1) = (0, 0)
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if (move == 'U'):
                y += 1
            elif (move == 'D'):
                y -= 1
            elif (move == 'R'):
                x += 1
            elif (move == 'L'):
                x -= 1
        
        return x == 0 and y == 0
        
"""
Time Complexity : O(n)
Space Complexity: O(1)
"""

s = Solution()
answer = s.judgeCircle("UD")
print(answer)

answer1 = s.judgeCircle("UULLDR")
print(answer1)