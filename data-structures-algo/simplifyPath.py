import unittest

# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.
class Solution:
    def simplifyPath(self, path: str) -> str:
      stack = []
      for dir in path.split('/'):
        if dir == '..':
          if stack:
            stack.pop()
        elif dir == '.' or dir == '':
          continue
        else:
            stack.append(dir)
      result = '/' + ('/'.join(stack))
      return result


class TestSimplifyPath(unittest.TestCase):
  def setUp(self):
    self.solution = Solution()

  def test_basic_path(self):
    self.assertEqual(self.solution.simplifyPath("/home/"), "/home")

  def test_remove_trailing_slash(self):
    self.assertEqual(
      self.solution.simplifyPath("/home/"),
      "/home",
      "Should remove trailing slash"
    )

  def test_multiple_slashes(self):
    self.assertEqual(
      self.solution.simplifyPath("/home//foo/"),
      "/home/foo",
      "Should replace multiple slashes with single slash"
    )

  def test_parent_directory(self):
    self.assertEqual(
      self.solution.simplifyPath("/home/user/Documents/../Pictures"),
      "/home/user/Pictures",
      "Should handle parent directory navigation"
    )

  def test_root_parent(self):
    self.assertEqual(
      self.solution.simplifyPath("/../"),
      "/",
      "Going above root should return root"
    )

  def test_complex_path(self):
    self.assertEqual(
      self.solution.simplifyPath("/.../a/../b/c/../d/./"),
      "/.../b/d",
      "Should handle complex path with valid ... directory"
    )

if __name__ == "__main__":
    unittest.main()

        