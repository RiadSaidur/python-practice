from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []

    def preOrder(root):
      if not root: return
      result.append(root.val)
      preOrder(root.left)
      preOrder(root.right)

    preOrder(root)
    return result

  