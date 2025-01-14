# If left or right exist  and it would be bigger than the current length, return early


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    """Binary tree node with value and optional left and right children."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """Solution class containing methods to solve binary tree problems."""
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if node.left is None:
                return 1 + dfs(node.right)
            if node.right is None:
                return 1 + dfs(node.left)
            return 1 + min(dfs(node.left), dfs(node.right))
        return dfs(root)


def test_minDepth():
    # Create a Solution instance
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution.minDepth(root1) == 2, "Test case 1 failed"

    # Test case 2: [2,null,3,null,4,null,5,null,6]
    #     2
    #      \
    #       3
    #        \
    #         4
    #          \
    #           5
    #            \
    #             6
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    assert solution.minDepth(root2) == 5, "Test case 2 failed"

    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test_minDepth()
        