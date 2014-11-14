# *********************************************
# Source : https://oj.leetcode.com/problems/valid-sudoku/
# Author : wizcabbit
# Date   : 2014-11-01

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# A partially filled sudoku which is valid.
# Note:
#   A valid Sudoku board (partially filled) is not necessarily solvable.
#   Only the filled cells need to be validated.
# *********************************************

width = 9

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
      rowMatrix = self.getValidMatrix()
      columnMatrix = self.getValidMatrix()
      groupMatrix = self.getValidMatrix()

      if len(board) != width:
        return False

      for i in range(width):
        if len(board[i]) != width:
          return False

        for j in range(width):
          if board[i][j] == '.':
            continue

          cell = int(board[i][j]) - 1
          # Validate Rows
          if rowMatrix[i][cell]:
            return False
          # Validate Columns
          if columnMatrix[j][cell]:
            return False
          # Validate Groups
          if groupMatrix[(i // 3) * 3 + j //3][cell]:
            return False

          rowMatrix[i][cell] = True
          columnMatrix[j][cell] = True
          groupMatrix[(i // 3) * 3 + j //3][cell] = True

      return True

    # @return a 9x9 matrix, filled with False
    def getValidMatrix(self):
      result = []
      for i in range(width):
        result.append([])
        for j in range(width):
          result[i].append(False)
      return result
