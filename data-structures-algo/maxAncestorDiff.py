from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], currMin: int, currMax: int) -> int:
            currMin = min(currMin, node.val)
            currMax = max(currMax, node.val)
            print(currMax - currMin)
            if not node.left and not node.right:
                return currMax - currMin
            if not node.left:
                return dfs(node.right, currMin, currMax)
            if not node.right:
                return dfs(node.left, currMin, currMax)
            return max(dfs(node.left, currMin, currMax), dfs(node.right, currMin, currMax))

        return dfs(root, root.val, root.val)


            

        



# Test cases
def test_maxAncestorDiff():
    # Helper function to create a binary tree from a list
    def createTree(values, index=0):
        if index >= len(values) or values[index] is None:
            return None

        root = TreeNode(values[index])
        root.left = createTree(values, 2 * index + 1)
        root.right = createTree(values, 2 * index + 2)
        return root

    solution = Solution()

    # # Test case 1: [8,3,10,1,6,null,14,null,null,4,7,13]
    # tree1_values = [8,3,10,1,6,None,14,None,None,4,7,None,13]
    # tree1 = createTree(tree1_values)
    # assert solution.maxAncestorDiff(tree1) == 7, "Test case 1 failed"
    
    # Test case 2: [1,null,2,null,0,3]
    tree2_values = [1,None,2,None,0,3]
    tree2 = createTree(tree2_values)
    assert solution.maxAncestorDiff(tree2) == 3, "Test case 2 failed"
    
    print("All test cases passed!")

# Run tests
if __name__ == "__main__":
    test_maxAncestorDiff()
    