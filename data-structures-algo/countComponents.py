# Create adjacency list
# Go through each node/key in list, see children until queue
# once the queue is empty (i.e. no more children exist, ans++ )
# haven't seen => ans++, add to seen

from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
          graph[x].append(y)
          graph[y].append(x)

        seen = set()
        ans = 0

        def bfs(start: int):
          q = deque([start])
          while len(q) != 0:
            node = q.pop()
            for child in graph[node]:
              if child not in seen:
                seen.add(child)
                q.appendleft(child)

        for node in range(n):
          if node not in seen:
            ans += 1
            bfs(node)

        return ans
