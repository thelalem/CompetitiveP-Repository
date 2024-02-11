from collections import defaultdict
class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        dc = defaultdict(int)
        for index,num in enumerate(nums):
            dc[num] = index
        for current,new in operations:
            if current in dc:
                pos = dc[current]
                nums[pos] = new
                dc[new] = pos
                del dc[current]
        return nums