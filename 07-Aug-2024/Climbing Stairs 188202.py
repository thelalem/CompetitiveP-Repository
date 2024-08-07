# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)

        def dp(n:int) -> int:
            if n < 3:
                return n
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)

            return memo[n]
        return dp(n)