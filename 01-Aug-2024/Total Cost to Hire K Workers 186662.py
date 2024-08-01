# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = 0
        r = len(costs) - 1
        lh = []
        rh = []

        total = 0
        while k > 0:
            while len(lh) < candidates and l <= r:
                heapq.heappush(lh, (costs[l], l))
                l += 1
            
            while len(rh) < candidates and l <= r:
                heapq.heappush(rh, (costs[r], r))
                r -= 1

            left_min = lh[0] if lh else (float('inf'), None)
            right_min = rh[0] if rh else (float('inf'), None)

            if left_min <= right_min:
                total += left_min[0]
                heapq.heappop(lh)
            else:
                total += right_min[0]
                heapq.heappop(rh)

            k -= 1

        return total