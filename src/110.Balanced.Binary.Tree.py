# *********************************************

# Source : https://oj.leetcode.com/problems/balanced-binary-tree/
# Author : wizcabbit
# Date   : 2014-11-12

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# *********************************************

class Solution:
  # @param root, a tree node
  # @return a boolean
  def isBalanced(self, root):
    return self.getBalanceHeight(root) != -1

  # @param root, a tree node
  # @return a int, if the root is balanced return height, or return -1
  def getBalanceHeight(self, root):
    if root is None:
      return 0;

    leftHeight = self.getBalanceHeight(root.left)
    # if left child tree is not balanced, return -1 directly to stop recursion
    if leftHeight < 0:
      return -1

    rightHeight = self.getBalanceHeight(root.right)
    # if right child tree is not balanced, return -1 directly to stop recursion
    if rightHeight < 0:
      return -1

    if math.fabs(leftHeight - rightHeight) > 1:
      return -1
    return max(leftHeight, rightHeight) + 1
