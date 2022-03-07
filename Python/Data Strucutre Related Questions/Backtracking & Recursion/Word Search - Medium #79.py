"""
Word Search - Medium #079

Given a 2D board and a word, find if the word exists in the grid.
- The word can be constructed from letters of sequentially adjacent cells.
- "Adjacent" cells are those horizontally or vertically neighbouring.
- The same letter cell may not be used more than once.


Example:

Input:

board =
[
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = "ABCCED"

Output: True

"""

class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]


    def solution(self, board, word, x, y, cur):
        if (x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
            return False

        cur += board[x][y]

        if (len(cur) > len(word)):
            return False
        
        if (cur[len(cur) - 1] != word[len(cur) - 1]):
            return False

        if (cur == word):
            return True

        temp = board[x][y]
        board[x][y] = ' '

        for i in range(4):
            if (self.solution(board, word, x + dx[i], y + dy[i], cur)):
                return True

        board[x][y] = temp
        return False


    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        if (len(word) == 0):
            return True
        n = len(board)
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if (word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
        return False

    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""