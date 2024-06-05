# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        sub = []
        def back(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            back(i+1)
            sub.pop()
            back(i+1)

        back(0)
        return res
            