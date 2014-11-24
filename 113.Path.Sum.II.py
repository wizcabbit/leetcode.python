# *********************************************
# Source : https://oj.leetcode.com/problems/path-sum-ii/
# Author : wizcabbit
# Date   : 2014-11-24

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# *********************************************

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
      return self._pathSum(root, sum, [], [])

    def _pathSum(self, root, sum, path, result):
      if root is None:
        return result

      if sum == root.val and root.left is None and root.right is None:
        return result + [path + [root.val]]
      else:
        return self._pathSum(root.left, sum - root.val, path + [root.val], result) + self._pathSum(root.right, sum - root.val, path + [root.val], result)
