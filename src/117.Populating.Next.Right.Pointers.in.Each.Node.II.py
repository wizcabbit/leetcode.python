# *********************************************
# Source : https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Author : wizcabbit
# Date   : 2014-10-30

# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:
#   You may only use constant extra space.

# For example,
# Given the following binary tree,
#         1
#       /  \
#      2    3
#     / \    \
#    4   5    7

# After calling your function, the tree should look like:
#         1 -> NULL
#       /  \
#      2 -> 3 -> NULL
#     / \    \
#    4-> 5 -> 7 -> NULL
# *********************************************

class Solution:
  # @param root, a tree node
  # @return nothing
  def connect(self, root):
    head = None;        # head of next layer
    previous = None;    # previous non-blank node on the next layer
    current = root;     # current node of current layer

    while current is not None:
      while current is not None:
        if current.left is not None:
          if previous is not None:
            previous.next = current.left;
          else:
            # previous is None, means current is layer's first node, so update head to current.left, means next layer's first node
            head = current.left;
          previous = current.left;
        if current.right is not None:
          if previous is not None:
            previous.next = current.right;
          else:
            head = current.right;
          previous = current.right;
        # Lead to current layer's next
        current = current.next;
      # Swtich to next layer
      current = head;
      head = None;
      previous = None;
