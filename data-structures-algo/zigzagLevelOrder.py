from typing import Optional, List
import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
          return []
        next_level = deque([root])
        ans = []
        while next_level:
          curr_level = next_level
          ans.append([node.val for node in next_level])
          depth = len(ans)
          next_level = deque()
          # if depth is odd, go right to left
          if depth % 2 == 1:
            for node in reversed(curr_level):
              if node.right:
                next_level.append(node.right)
              if node.left:
                next_level.append(node.left)
          else:
            for node in reversed(curr_level):
              if node.left:
                next_level.append(node.left)
              if node.right:
                next_level.append(node.right)

        return ans

          
            