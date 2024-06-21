# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,col = len(grid),len(grid[0])
        visit = set()
        islands = 0
        def dfs(r,c):
            if(r,c) in visit or r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == "0":
                return
            visit.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr,dc in directions:
                dfs(r + dr, c+dc)
                
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    islands += 1
        return islands
