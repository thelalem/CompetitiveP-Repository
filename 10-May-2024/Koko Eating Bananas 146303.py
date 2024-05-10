# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2

            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        return res

