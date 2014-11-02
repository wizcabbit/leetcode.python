# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
