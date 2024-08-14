# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        directions = {
            1: {'left': (0, -1), 'right': (0, 1)},
            2: {'up': (-1, 0), 'down': (1, 0)},
            3: {'left': (0, -1), 'down': (1, 0)},
            4: {'right': (0, 1), 'down': (1, 0)},
            5: {'left': (0, -1), 'up': (-1, 0)},
            6: {'right': (0, 1), 'up': (-1, 0)}
        }

        def is_valid(x, y, from_dir):
            if not (0 <= x < m and 0 <= y < n):
                return False
            next_street = grid[x][y]
            if from_dir == 'left' and next_street in [1, 4, 6]:
                return True
            if from_dir == 'right' and next_street in [1, 3, 5]:
                return True
            if from_dir == 'up' and next_street in [2, 3, 4]:
                return True
            if from_dir == 'down' and next_street in [2, 5, 6]:
                return True
            return False
        
        stack = [(0, 0)] 
        visited = set()
        
        while stack:
            x, y = stack.pop() 
            if (x, y) == (m - 1, n - 1):  
                return True
            visited.add((x, y))  
            for direction, (dx, dy) in directions[grid[x][y]].items():
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, direction) and (nx, ny) not in visited:
                    stack.append((nx, ny))
        
        return False