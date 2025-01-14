from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ans = 0

        def valid(row: int, col: int) -> bool:
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row: int, col: int):
            area = 1
            grid[row][col] = 0
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col):
                    area += dfs(next_row, next_col)
            return area

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))

        return ans
