# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
      previous = None
      firstChild = None
      if not (root is None):
          root.next = None

      while True:
        if (root is None):
          break

        if root.left is None:
          if root.right is None:
            None
          else:
            if not (previous is None):
              previous.next = root.right

            previous = root.right
            if firstChild is None:
              firstChild = root.right
        else:
          if not (previous is None):
              previous.next = root.left

          if firstChild is None:
              firstChild = root.left

          if root.right is None:
            previous = root.left
          else:
            root.left.next = root.right
            previous = root.right

        if root.next is None:
          if not (previous is None):
            previous.next = None
          root = firstChild
          firstChild = None
          previous = None
        else:
          root =  root.next


