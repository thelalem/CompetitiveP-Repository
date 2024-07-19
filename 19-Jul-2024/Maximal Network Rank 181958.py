# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        road_count = [0] * n
        adj = defaultdict(set)
    
        for a, b in roads:
            road_count[a] += 1
            road_count[b] += 1
            adj[a].add(b)
            adj[b].add(a)
        
        max_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = road_count[i] + road_count[j]
               
                if j in adj[i]:
                    rank -= 1

                max_rank = max(max_rank, rank)
        
        return max_rank