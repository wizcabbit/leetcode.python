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

    def getValidMatrix(self):
      result = []
      for i in range(width):
        result.append([])
        for j in range(width):
          result[i].append(False)
      return result

def test(board, expect):
  solution = Solution()
  if solution.isValidSudoku(board) != expect:
    print("Except: " + str(expect) + " But: " + str(not expect))
  else:
    print("PASS!")

board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
test(board, True)
