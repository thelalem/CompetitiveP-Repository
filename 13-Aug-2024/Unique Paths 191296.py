# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[-1]*n for _ in range(m)]

        def dp(i,j):
            if i == 0 or j == 0:
                return 1
            if d[i][j] != -1:
                return d[i][j]

            d[i][j] = dp(i-1,j) + dp(i,j-1)
            return d[i][j]
        return dp(m-1,n-1)