# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
 
        hold = [0] * n  
        sold = [0] * n  
        rest = [0] * n  
        hold[0] = -prices[0]  
        sold[0] = 0  
        rest[0] = 0  
        for i in range(1, n):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])  
            sold[i] = hold[i-1] + prices[i]  
            rest[i] = max(rest[i-1], sold[i-1])  
        
       
        return max(sold[n-1], rest[n-1])