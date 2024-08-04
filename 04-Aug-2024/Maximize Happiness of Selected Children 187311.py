# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_heap = []
        for h in happiness:
            heapq.heappush(max_heap, -h)
        
        max_sum = 0
        counter = 0
        
        for _ in range(k):
            max_value = -heapq.heappop(max_heap)
            max_sum += max(0,max_value - counter)
            counter += 1
        return max_sum