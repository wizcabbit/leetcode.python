# Solution 1 in 2014.11.1
# Looks terrible judgement, the DNF is so complicated

class Solution1:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        i = 0
        hasE = False
        hasDot = False
        hasNum = False
        hasPre = False
        hasBlank = False
        lastNonBlank = None

        while i < len(s):
          c = s[i]

          if c == '0':
            hasNum = True
            lastNonBlank = c
            if hasBlank:
              return False;
          elif c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if hasBlank:
              return False;
            hasNum = True
            lastNonBlank = c
            i = i + 1
            continue
          elif c == 'e':
            if hasBlank:
              return False;
            if (not hasNum) or hasE:
              return False;
            hasE = True
            lastNonBlank = c
          elif c == '.':
            if hasBlank:
              return False;
            if hasE or hasDot:
              return False
            hasDot = True
            lastNonBlank = c
          elif c == ' ':
            if hasNum or hasDot or hasE or hasPre:
              hasBlank = True
            i = i + 1
            continue
          elif c == '-' or c == '+':
            if hasBlank:
              return False;
            hasPre = True

            if not hasNum and not hasDot:
              i = i + 1
              continue
            elif hasE and s[i - 1] == 'e':
              i = i + 1
              continue
            else:
              return False
          else:
            return False
          i = i + 1

        if not hasNum:
          return False
        if i > 0:
          c = s[i - 1]

          if lastNonBlank == 'e':
            return False
        return True

# Solution 2 in 2014.11.1
# Use python's library

class Solution2:
    def isNumber(self, s):
        try:
            float(s)                 # If error is shown then print False else True
            return True
        except:
            return False

def test(s, expect):
  solution = Solution2()
  if solution.isNumber(s) != expect:
    print("'" + s + "'" + " EXPECT: " + str(expect) + " BUT " + str(not expect))

print("START")

test("    ", False)
test("0", True)
test("1", True)
test(" 1", True)
test("1 ", True)
test(" 1 ", True)
test("0.1", True)
test("1.1", True)
test("1.", True)
test(".1", True)
test("1.   ", True)
test("   .1", True)
test("01.   ", True)
test("   .01", True)
test(".1000", True)
test("    .1000   ", True)
test("1e3", True)
test(" 1e3  ", True)
test("1.2e3", True)
test("1.2e5   ", True)
test("   1.2e4", True)
test("e3", False)
test("0", True)
test("3e", False)
test("3e  ", False)
test("  3  e ", False)
test("+1", True)
test("+1e3", True)
test("+1.3e3", True)
test(" +1e3", True)
test(" -1e3  ", True)
test(" -1e+3  ", True)
test(" -1e-3  ", True)
test("- 1e3", False)
test(". 4 ", False)
test("6. 4 ", False)

print("END")
