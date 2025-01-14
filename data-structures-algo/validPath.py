from typing import List, Dict
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen = set()

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        return graphBFS(source, destination, graph)

        # def dfs(node_id: int) -> bool:
        #     if node_id == destination:
        #         return True
        #     res = []
        #     for neighbor in graph[node_id]:
        #         if neighbor not in seen:
        #             seen.add(neighbor)
        #             res.append(dfs(neighbor))
        #     return any(res)

        # return dfs(source)
        # return destination in seen


def graphBFS(start: int, end: int, graph: Dict[int, List[int]]) -> bool:
    q = deque([start])
    seen = set()

    while len(q) != 0:
        node = q.pop()
        if node == end:
            return True
        for child in graph[node]:
            if child not in seen:
                seen.add(child)
                q.appendleft(child)
    return False
