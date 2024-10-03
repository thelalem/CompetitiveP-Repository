# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = defaultdict(list)
        
        for ai, bi in richer:
            adj[bi].append(ai)
        
        answer = [-1] * n
        
        def dfs(x):
            if answer[x] != -1:
                return answer[x]
            
            answer[x] = x
            for neighbor in adj[x]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[answer[x]]:
                    answer[x] = candidate
            
            return answer[x]
            
        for i in range(n):
            dfs(i)
        
        return answer