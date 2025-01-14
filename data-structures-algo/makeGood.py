import unittest

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
          if stack:
            if stack[-1].lower() == c.lower() and stack[-1] != c:
              stack.pop()
            else:
              stack.append(c)
          else:
            stack.append(c)
        
        return ''.join(stack)


class TestMakeGood(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        self.assertEqual(self.solution.makeGood("leEeetcode"), "leetcode")
    
    def test_example2(self):
        self.assertEqual(self.solution.makeGood("abBAcC"), "")
    
    def test_example3(self):
        self.assertEqual(self.solution.makeGood("s"), "s")

if __name__ == '__main__':
    unittest.main()
        