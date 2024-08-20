# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp =defaultdict(int)

        for i in range(len(questions)-1,-1,-1):
            dp[i] = max(questions[i][0] + dp[i+1+questions[i][1]] , dp[i+1])

        return dp[0]