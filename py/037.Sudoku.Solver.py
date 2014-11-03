width = 9

class Solution:
    validCount = 0
    loopCount = 0

    def solveSudoku(self, board):
      self.solveSudokuTask(board)

    def solveSudokuTask(self, board):
      for i in range(width):
        for j in range(width):
          if board[i][j] != ".":
            continue
          for k in range(width):
            self.loopCount += 1
            board[i][j] = str(k + 1)
            if self.isValidSudoku(board, i, j):
              if self.solveSudokuTask(board):
                return True
            board[i][j] = '.'
          return False
      return True

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

def test(board):
  testBoard = []
  for i in range(width):
    testBoard.append([])
    for j in range(width):
      testBoard[i].append(board[i][j])
  solution = Solution()
  solution.solveSudoku(testBoard)

  print(solution.loopCount)

board = [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
test(board)
