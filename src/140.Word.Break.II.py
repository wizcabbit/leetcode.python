# *********************************************
# Source : https://oj.leetcode.com/problems/word-break-ii/
# Author : wizcabbit
# Date   : 2014-10-05

# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].
# *********************************************

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
