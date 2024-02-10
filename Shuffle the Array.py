class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        i = 0
        j = n
        lists = []
        while i < n:
            lists.append(nums[i])
            lists.append(nums[j])
            i += 1
            j += 1
        return lists