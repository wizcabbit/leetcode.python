# *********************************************
# Source : https://oj.leetcode.com/problems/valid-sudoku/
# Author : wizcabbit
# Date   : 2014-11-02

# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# *********************************************

width = 9

class Solution:
    validCount = 0

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
      for i in range(width):
        for j in range(width):
          if board[i][j] != ".":
            continue
          for k in range(width):
            board[i][j] = str(k + 1)
            if self.isValidSudoku(board, i, j):
              if self.solveSudokuTask(board):
                return True
            # Attempt fail, backtracking
            board[i][j] = '.'
          return False
      return True

    # @param board, a 9x9 2D array
    # @param x, row count of changed value
    # @param y, rolumn count of changed value
    # Validate if the sudoku is valid after (x,y)'s value changed
    # @return a boolean, if the sudoku is valid
    def isValidSudoku(self, board, x, y):
      self.validCount += 1
      for i in range(width):
        if i != x and board[i][y] == board[x][y]:
          return False
      for k in range(width):
        if k != y and board[x][k] == board[x][y]:
          return False
      for m in range(3 * (x // 3), 3 * (x // 3 + 1)):
        for n in range(3 * (y // 3), 3 * (y // 3 + 1)):
          if (m != x and n != y) and board[m][n] == board[x][y]:
            return False
      return True
