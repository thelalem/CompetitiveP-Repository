from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        twosum = defaultdict(list)
        for i,num in enumerate(nums):
            diff = target - num
            if diff in twosum:
                print(twosum)
                return [twosum[diff] , i]
            twosum[num] = i