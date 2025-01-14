class Solution:
    def simplifyPath(s: str) -> str:
      stack = []
      if s[0] != '/':
        stack.append('/')
      for c in s:
        if stack[-1] = '/' and c = '/'