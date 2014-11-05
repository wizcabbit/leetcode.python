class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    map = {};
    return self.findList(s, dict, map)

  def findList(self, s, dict, map):
    if (map.has_key(s)):
      return map[s]

    answerList = []
    length = len(s)

    if length <= 0:
      return answerList

    for i in range(1, length + 1):
      prefix = s[0 : i]
      if prefix in dict:
        if i == length:
          answerList.append(prefix)
        else:
          temp = self.findList(s[i : length], dict, map)
          for tmp in temp:
            tmp = prefix + " " + tmp
            answerList.append(tmp)
    map[s] = answerList
    print(map)
    return answerList



solution = Solution()

def test(s, dict, expect):
  r = solution.wordBreak(s, dict)
  print(r)

test("1234", ["12", "1", "23", "34","2"], True)
