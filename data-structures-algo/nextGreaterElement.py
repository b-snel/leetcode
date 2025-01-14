# All values in nums1 must be in nums2
# nums2[j] > nums1[i]
# Solution should not run longer than the total length of both nums1 and nums2 array
# We should be able to tell if 

import unittest
from typing import List
from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        queue = deque()
        # for i in range(len(nums2)):


class TestNextGreaterElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        expected = [-1, 3, -1]
        result = self.solution.nextGreaterElement(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        expected = [3, -1]
        result = self.solution.nextGreaterElement(nums1, nums2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()