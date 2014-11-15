# *********************************************
# Source : https://oj.leetcode.com/problems/word-break/
# Author : wizcabbit
# Date   : 2014-10-05

# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".
# *********************************************

class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    sLen = len(s)
    possible = [False for i in range(sLen + 1)]
    possible[0] = True

    for i in range(sLen):
      for j in range(i + 1):
        if possible[j] and s[j:i + 1] in dict:
            possible[i + 1] = True
            break;

    return possible[sLen]
