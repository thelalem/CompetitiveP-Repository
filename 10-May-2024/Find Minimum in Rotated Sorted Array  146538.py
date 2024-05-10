# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1 or nums[0] <= nums[-1]:
            return nums[0]
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]