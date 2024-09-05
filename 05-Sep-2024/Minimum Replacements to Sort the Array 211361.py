# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                num_parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1] 
                operations += num_parts - 1 
                nums[i] = nums[i] // num_parts
        
        return operations