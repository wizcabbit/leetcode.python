# *********************************************
# Source : https://oj.leetcode.com/problems/recover-binary-search-tree/
# Author : wizcabbit
# Date   : 2014-11-09

# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.

# Note:
#   A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# *********************************************

class Solution:
    _previous = None
    _swapA = _swapB = None

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
      self._coverTree(root)

      # Swap the node's value
      if self._swapA is not None and self._swapB is not None:
        temp = self._swapA.val
        self._swapA.val = self._swapB.val
        self._swapB.val = temp

      return root

    # @param root, a tree node
    # @return a tree node
    def _coverTree(self, root):
      if root is None or root.val is None:
        return

      self._coverTree(root.left)

      if self._previous is not None and self._previous.val is not None:
        if self._previous.val > root.val:
          if self._swapA is None:
            self._swapA = self._previous
          self._swapB = root

      self._previous = root
      self._coverTree(root.right)
