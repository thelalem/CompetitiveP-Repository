# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        ans = 0
        for i in range(1,mn+1):
            if mn%i == 0 and mx%i == 0:
                ans = max(ans,i)
        return ans
        