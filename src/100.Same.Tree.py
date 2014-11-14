# *********************************************
# Source : https://oj.leetcode.com/problems/same-tree/
# Author : wizcabbit
# Date   : 2014-11-12

# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
# *********************************************


class Solution:
  # @param p, a tree node
  # @param q, a tree node
  # @return a boolean
  def isSameTree(self, p, q):
    if p is None and q is None:
      return True
    if p is None or q is None or p.val != q.val:
      return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
