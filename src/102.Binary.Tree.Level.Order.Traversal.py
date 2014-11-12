# *********************************************

# Source : https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
# Author : wizcabbit
# Date   : 2014-11-12

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# *********************************************

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):

