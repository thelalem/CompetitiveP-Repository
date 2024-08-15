# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        last_level = len(coins)
        memo = {}
        def rec(level,amount):
            if amount == 0:
                return 1
            if level == last_level:
                return 0 
            if (level,amount) in memo:
                return memo[(level,amount)]
            
            count= 0
            for k in range(amount // coins[level] + 1):
                count += rec(level+1, amount - k*coins[level])
            
            memo[(level,amount)] = count
            return count
        
        return rec(0,amount)