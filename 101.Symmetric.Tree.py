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

# Solution 1 in 2014.11.2
# It failed, too much complicate, I can't controll it
class Solution1:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
      curLayer = [root]
      curLayerWidth = 1
      childLayer = []
      childLayerEmpty = True

      while len(curLayer) > 0:
        r = curLayer.pop(0)
        if not (r is None):
          childLayer.append(r.left)
          childLayer.append(r.right)
          childLayerEmpty = False
        else:
          childLayer.append(None)
          childLayer.append(None)

        if len(curLayer) == 0:
          if childLayerEmpty:
            return True
          curLayer = childLayer
          curLayerWidth = curLayerWidth * 2
          childLayer = []
          childLayerEmpty = True

          if not self.valid(curLayer, curLayerWidth):
            return False
      return True

    def valid(self, curLayer, curLayerWidth):
      index = 0
      curLen = len(curLayer)
      while index < curLen and index < curLayerWidth / 2:
        nodeA = curLayer[index]
        nodeBi = curLayerWidth - index - 1
        if (nodeBi >= curLen):
          nodeB = None
        else:
          nodeB = curLayer[nodeBi]

        if not self.equal(nodeA, nodeB):
          for i in curLayer:
            print(i)
          return False

        index = index + 1
      return True

    def equal(self, nodeA, nodeB):
      if nodeA is None:
        if nodeB is None:
          return True
        else:
          if nodeB.val is None:
            return True
          else:
            return False
      elif nodeA.val is None:
        if nodeB is None:
          return True
        else:
          return nodeB.val == None
      else:
        if nodeB is None:
          return False
        else:
          return nodeA.val == nodeB.val

# Solution 2 in 2014.11.2
# It works, recursively
class Solution2:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False

# Solution 2 in 2014.11.2
# It works, iteratively
class Solution3:
  def isSymmetric(self, root):
    if root is None:
      return True

    stack = [[root.left, root.right]]

    while len(stack) > 0:
      pair = stack.pop(0)
      left = pair[0]
      right = pair[1]

      if left is None and right is None:
        continue
      if left is None or right is None:
        return False
      if left.val == right.val:
        stack.insert(0, [left.left, right.right])

        stack.insert(0, [left.right, right.left])
      else:
        return False
    return True


def test(s, expect):
  solution = Solution3()
  print("*****Testing: '" + s + "'*****")
  if solution.isSymmetric(initTree(s)) != expect:
    print("EXPECT: " + str(expect) + " BUT " + str(not expect))
  else:
    print("SUCCESS")

test("", True)
test("1", True)
test("1,2,2", True)
test("1,2,3", False)
test("1,2,3,4", False)
test("1,2,3,4,#", False)
test("1,3,3,4,#,#,4", True)
test("1,4,4,5,#,#,5,6,#,#,6", True)
test("1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5", True)

