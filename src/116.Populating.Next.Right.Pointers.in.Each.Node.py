# *********************************************
# Source : https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Author : wizcabbit
# Date   : 2014-10-29

# Given a binary tree

#    struct TreeLinkNode {
#      TreeLinkNode *left;
#      TreeLinkNode *right;
#      TreeLinkNode *next;
#    }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:
#   You may only use constant extra space.
#   You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# *********************************************

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
      self._connect(root, None);

    # @param root, a tree node
    # @param sibling, current node's sibling node
    # @return nothing
    def _connect(self, root, sibling):
      if root is None:
        return;
      else:
        root.next = sibling;

      self._connect(root.left, root.right);

      if sibling is not None:
        # Connect current node's right and sibling's left
        self._connect(root.right, sibling.left);
      else:
        self._connect(root.right, None);
