# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_board_value(x):
            r = n - 1 - (x // n)
            c = (x % n) if (x // n) % 2 == 0 else n - 1 - (x % n)
            return board[r][c]
        visited = set()
        queue = deque([(1, 0)])  
        
        while queue:
            curr, moves = queue.popleft()
            if curr == n * n:
                return moves
            for next_square in range(curr + 1, min(curr + 6, n * n) + 1):
                board_value = get_board_value(next_square - 1)
                dest = next_square if board_value == -1 else board_value
                
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        
        return -1