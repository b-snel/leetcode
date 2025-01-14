import unittest
from closestValue import Solution, TreeNode
from typing import List, Optional

def buildTree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = buildTree(values, 2 * index + 1)
    root.right = buildTree(values, 2 * index + 2)
    return root

class TestClosestValue(unittest.TestCase):
    def test_complex_tree(self):
        values = [2,0,33,None,1,25,40,None,None,11,31,34,45,10,18,29,32,None,None,35,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None,None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6]
        target = 0.428571
        
        root = buildTree(values)
        solution = Solution()
        result = solution.closestValue(root, target)
        
        self.assertEqual(result, 0)  # 0 is closest to 0.428571

if __name__ == '__main__':
    unittest.main() 