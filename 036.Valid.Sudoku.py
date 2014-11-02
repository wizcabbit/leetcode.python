  width = 9

  class Solution:
      # @param board, a 9x9 2D array
      # @return a boolean
      def isValidSudoku(self, board):
        rowMatrix = self.getValidMatrix()
        columnMatrix = self.getValidMatrix()
        groupMatrix = self.getValidMatrix()

        i = 0
        j = 0

        if len(board) != width:
          return False

        while i < width:
          if len(board[i]) != width:
            return False

          while j < width:
            if board[i][j] != '.':
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

            j = j  + 1
          i = i + 1
          j = 0

        return True

      def getValidMatrix(self):
        result = []
        i = 0
        j = 0
        while i < width:
          result.append([])
          while j < width:
            result[i].append(False)
            j = j + 1
          i = i + 1
          j = 0
        return result

def test(board, expect):
  solution = Solution()
  if solution.isValidSudoku(board) != expect:
    print("Except: " + str(expect) + " But: " + str(not expect))
  else:
    print("PASS!")

board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
test(board, True)
