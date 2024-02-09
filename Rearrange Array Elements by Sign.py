class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        lists = [0]*len(nums)
        j = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                lists[j] = nums[i]
                j += 2
            else:
                lists[k] = nums[i]
                k += 2
        return lists