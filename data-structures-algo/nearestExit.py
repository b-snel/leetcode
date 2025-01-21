from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        q = deque([(entrance[0], entrance[1], 0)])  # row, col, steps
        maze[entrance[0]][entrance[1]] = "+"

        while q:
            row, col, steps = q.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and maze[next_row][next_col] == "."
                ):
                    if (
                        next_row == 0
                        or next_row == rows - 1
                        or next_col == 0
                        or next_col == cols - 1
                    ):
                        return steps + 1
                    maze[next_row][next_col] = "+"
                    q.append((next_row, next_col, steps + 1))

        return -1
