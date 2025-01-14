from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
          if not node:
            return TreeNode(val)
          if val < node.val:
            node.left = dfs(node.left)
          else:
            node.right = dfs(node.right)
          return node

        return dfs(root)