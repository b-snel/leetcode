from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return None
            if target == node.val:
                return node.val
            if target < node.val:
                left = dfs(node.left)
                if left is None or abs(node.val - target) < abs(left - target):
                    return node.val
                return left
            right = dfs(node.right)
            if right is None or abs(node.val - target) <= abs(right - target):
                return node.val
            return right
        return dfs(root)
