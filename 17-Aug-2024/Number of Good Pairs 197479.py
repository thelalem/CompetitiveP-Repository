# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dc = Counter(nums)
        count = 0
        for i in dc:
            n = dc[i]
            if n > 1:
                count += n * (n - 1)//2
        return count

