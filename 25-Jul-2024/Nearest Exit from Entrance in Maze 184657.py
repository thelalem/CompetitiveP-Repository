# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        start_row, start_col = entrance
        queue = deque([(start_row, start_col, 0)])
        visited = set((start_row, start_col))
        
        def is_exit(r, c):
            return (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and (r != start_row or c != start_col)
        
        while queue:
            r, c, steps = queue.popleft()
            
            if is_exit(r, c):
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        
        return -1