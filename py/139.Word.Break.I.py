class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  loop = 0
  def wordBreak(self, s, dict):
    sLen = len(s)
    possible = [False for i in range(sLen + 1)]
    possible[0] = True

    for i in range(sLen):
      for j in range(i + 1):
        self.loop += 1
        if possible[j] and s[j:i + 1] in dict:
            possible[i + 1] = True
            break;

    return possible[sLen]

solution = Solution()

def test(s, dict, expect):
  r = solution.wordBreak(s, dict)
  if r != expect:
    print(s + " in " + str(dict) + ", Except: " + str(expect) + " But: " + str(r))
  else:
    print("SUCCESS")
    print(solution.loop)

test("", [], True)
test("1", ["1"], True)
test("123", ["1"], False)
test("123", ["1","2","3"], True)
test("123", ["12","3"], True)
test("123", ["123","a"], True)
test("1aa1", ["1","a"], True)
