"""
Word Search - Medium #079

Given a 2D board and a word, find if the word exists in the grid.
- The word can be constructed from letters of sequentially adjacent cells.
- "Adjacent" cells are those horizontally or vertically neighbouring.
- The same letter cell may not be used more than once.

How to solve the problem:
- It would only make sense to start our search process when we find the first character of the given word.
  Otherwise, there's no point of traversing through the board to look for the given word.
- We can only connect letters that are adjacent. This means if we don't find the next character of the given word,
  we can assume that we can't form a word that matches the given word with the current combination.
- We should keep track of our current string to see how far it is from being the given word.

Steps:
- Loop over the board
- Check if the current character is the same as the first character in our input string,
  if it is, call our solution recursive function that will search for the rest of the characters
- If we didn't find the word from the recursive calls, simply continue looping until finding another character
  that matches the first character, and call the recursive function again to search for the rest of the characters

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

from typing import List

class Solution:
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    # The solution recursive function will take the following parameters:
    # board = board with different characters
    # word = word we need to find
    # x, y = position of the current character in the board
    # cur = current string we've found so far while searching for the word
    def solution(self, board, word, x, y, cur):
        # Check if the current position is out of bounds of the board,
        # or if the current character is already visited, if so, return False.
        if (x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
            return False

        cur += board[x][y]

        # Current combination can't be longer than the given word
        # If that's the case, return False
        if (len(cur) > len(word)):
            return False
        
        # If the last character of the current word and the given word do not match,
        # they're not the same word, thus return False
        if (cur[len(cur) - 1] != word[len(cur) - 1]):
            return False

        # If current word is same as the given word, return True
        if (cur == word):
            return True

        # Store the current charcter and mark the current position as visited ' '
        temp = board[x][y]
        board[x][y] = ' '

        # Start a loop of size 4, which is the # of neighbouring cells:
        # vertical up and down & horizontal up and down
        for i in range(4):
            # Check if the result of the recursive call with the same parameters except for the position,
            # move the position of the current character to the neighbouring cells
            if (self.solution(board, word, x + self.dx[i], y + self.dy[i], cur)):
                return True

        # If we reached this point, we didn't find the next character from the current word,
        # revert the visited neighbours with the original characters, 
        # and return False for word NOT FOUND with the current characters.
        board[x][y] = temp
        return False


    def wordSearch(self, board: List[List[str]], word: str) -> bool:
        # If the word is an empty string, simply return True
        if (len(word) == 0):
            return True

        # Loop over the board
        # n = y axis of the board
        n = len(board)
        for i in range(n):
            # m = x axis of the board
            m = len(board[i])
            for j in range(m):
                # If we've found the first matching character, call the recursive function
                if (word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
        return False

    

        

        
"""
Time Complexity : O()
Space Complexity: O()
"""