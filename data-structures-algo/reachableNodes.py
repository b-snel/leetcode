from typing import List, Dict
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        seen = [False] * n
        for node in restricted:
          seen[node] = True

        for x,y in edges:
          if not seen[x] and not seen[y]:
            graph[x].append(y)
            graph[y].append(x)

        ans = 0
        def dfs(node: int) -> int:
          if seen[node]:
            return
          nonlocal ans
          ans += 1
          seen[node] = True
          for neighbor in graph[node]:
            dfs(neighbor)

        dfs(0)
        return ans

          