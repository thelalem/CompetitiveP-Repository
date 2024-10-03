# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
    
        dp[0][row][column] = 1

        for m in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for move in moves:
                        new_r, new_c = r + move[0], c + move[1]
                        if 0 <= new_r < n and 0 <= new_c < n:
                            dp[m][new_r][new_c] += dp[m - 1][r][c] / 8
    
        total_probability = 0
        for r in range(n):
            for c in range(n):
                total_probability += dp[k][r][c]
        
        return total_probability