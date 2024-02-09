from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counter = Counter(nums)
        lists = []
        for key in counter:
            if counter[key] > len(nums)/3:
                lists.append(key)
        return lists