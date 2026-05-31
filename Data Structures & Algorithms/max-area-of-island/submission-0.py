class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        visited = [[0] * COLS for _ in range(ROWS)]


        def dfs(r, c):
            visited[r][c] = 1
            size = 1
            for dr, dc in directions:
                nr,nc = dr + r, dc + c
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                elif grid[nr][nc] and not visited[nr][nc]:
                    size += dfs(nr, nc)
            return size
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and not visited[r][c]:
                    res = max(res, dfs(r,c))
        return res
