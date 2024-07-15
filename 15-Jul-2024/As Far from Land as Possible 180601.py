# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append([r,c])

        res = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            r,c = q.popleft()

            res = grid[r][c]
            for dr,dc in directions:
                newR,newC = r+dr, c+dc
                if min(newR,newC) >= 0 and max(newR,newC) < n and grid[newR][newC] == 0:
                    q.append([newR,newC])
                    grid[newR][newC] = grid[r][c] + 1

        return res-1 if res > 1 else -1