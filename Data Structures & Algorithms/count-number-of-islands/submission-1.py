class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        res = 0

        def dfs(r,c):
            visited.add((r,c))
            for dr,dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue
                if (nr, nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr,nc)
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    dfs(r,c)
        return res
