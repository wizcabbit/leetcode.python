# *********************************************

# Source : https://oj.leetcode.com/problems/validate-binary-search-tree/
# Author : wizcabbit
# Date   : 2014-11-09

# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.

# *********************************************

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
      return self._isValidBST(root, -2147483647, 2147483647);

    # @param root, a tree node
    # @param min, min valid value
    # @param max, max valid value
    # @return a boolean
    def _isValidBST(self, root, min, max):
      if root is None or root.val is None:
        return True
      # Valid condition: smaller than max, bigger than min, left and right is both valid BST
      return root.val < max \
        and root.val > min \
        and self._isValidBST(root.left, min, root.val) \
        and self._isValidBST(root.right, root.val, max)
