# Solution 1 in 2014.11.1
# Looks terrible judgement, but it works ^_^. And the space / time maybe very good.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution1:
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


# Solution 2 in 2014.11.1
# from: https://oj.leetcode.com/discuss/3339/o-1-space-o-n-complexity-iterative-solution
# re-code it into python, and it needs some optimize

class Solution2:
  # @param root, a tree node
  # @return nothing
  def connect(self, root):
    head = None;
    previous = None;
    current = root;

    while not (current is None):
      while not (current is None):
        if not (current.left is None):
          if not (previous is None):
            previous.next = current.left;
          else:
            head = current.left;
          previous = current.left;
        if not (current.right is None):
          if not (previous is None):
            previous.next = current.right;
          else:
            head = current.right;
          previous = current.right;
        current = current.next;
      current = head;
      head = None;
      previous = None;
