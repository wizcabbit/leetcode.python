# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
      return self._isValidBST(root, -2147483647, 2147483647);

    def _isValidBST(self, root, min, max):
      if root is None or root.val is None:
        return True

      return root.val < max \
        and root.val > min \
        and self._isValidBST(root.left, min, root.val) \
        and self._isValidBST(root.right, root.val, max)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
      if self.val is None:
        return "None"
      else:
        return self.val

def initTree(str):
  nodes = str.split(',')
  if len(nodes) == 0:
    return None
  else:
    root = TreeNode(nodes[0])
    queue = [root]

  for node in nodes:
    n = queue.pop(0)
    if (node != "#"):
      n.val = node
    else:
      n.val = None

    n.left = TreeNode(None)
    n.right = TreeNode(None)
    queue.append(n.left)
    queue.append(n.right)

  return root

def test(s, expect):
  solution = Solution()
  print("Testing: " + s)
  if solution.isValidBST(initTree(s)) != expect:
    print("EXPECT: " + str(expect) + " BUT " + str(not expect))
  else:
    print("SUCCESS")

test("", True)
test("1", True)
test("1,1", False)
test("2,1,3", True)
test("5,1,6", True)
test("5,#,6", True)
test("10,5,15,#,#,6,20", False)

test("3,1,5,0,2,4,6", True)
test("3,1,5,0,2,4,6,#,#,#,3", False)
