# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
      self.connect_private(root, None);

    def connect_private(self, root, sibling):
      if root is None:
        return;
      else:
        root.next = sibling;

      self.connect_private(root.left, root.right);

      if not (sibling is None):
        self.connect_private(root.right, sibling.left);
      else:
        self.connect_private(root.right, None);