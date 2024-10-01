# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        n = len(nums)
        length = [1] * n  
        count = [1] * n   
        
        max_len = 0  
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
            max_len = max(max_len, length[i])
        result = sum(c for l, c in zip(length, count) if l == max_len)
        
        return result