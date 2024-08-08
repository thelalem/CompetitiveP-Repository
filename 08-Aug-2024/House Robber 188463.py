# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
    
        n = len(nums)
        dp = [0] * n
    
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
    
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
        return dp[-1]