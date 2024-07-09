# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            largest_pile -= largest_pile // 2
            heapq.heappush(max_heap, -largest_pile)
        
        return -sum(max_heap)
