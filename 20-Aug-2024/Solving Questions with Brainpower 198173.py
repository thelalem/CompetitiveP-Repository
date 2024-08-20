# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(questions):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(dfs(i+1),questions[i][0] + dfs(i+1+questions[i][1]))
            return cache[i]
        
        return dfs(0)