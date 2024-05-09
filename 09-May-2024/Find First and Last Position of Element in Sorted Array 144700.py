# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = r = mid
                while l > 0 and nums[l-1] == target:
                    l -= 1
                while r < len(nums) - 1 and nums[r+1] == target:
                    r += 1
                return [l,r]
        return [-1,-1]