from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node: Optional[TreeNode]) -> Optional[int]:
          if not node:
            return 0
          nonlocal diameter
          left = dfs(node.left)
          right = dfs(node.right)
          diameter = max(diameter, (left + right))
          return max(left, right) + 1
        dfs(root)
        return diameter

import unittest

class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Create tree: [1,2,3,4,5]
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_example_2(self):
        # Create tree: [1,2]
        #       1
        #      /
        #     2
        root = TreeNode(1)
        root.left = TreeNode(2)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)

    def test_empty_tree(self):
        self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

    def test_linear_tree(self):
        # Create tree: [1,2,null,3,null,4]
        #       1
        #      /
        #     2
        #    /
        #   3
        #  /
        # 4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_diameter_through_leaves(self):
        # Create tree where diameter goes through leaves
        #       1
        #      / \
        #     2   3
        #    /     \
        #   4       5
        #  /         \
        # 6           7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.left.left.left = TreeNode(6)
        root.right.right.right = TreeNode(7)
        
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 6)

if __name__ == '__main__':
    unittest.main()