# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []

        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            permu = self.permute(nums)
            for per in permu:
                per.append(n)
            res.extend(permu)
            nums.append(n)
        
        return res