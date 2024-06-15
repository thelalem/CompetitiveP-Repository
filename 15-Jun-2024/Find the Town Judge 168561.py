# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for dep,arr in trust:
            outgoing[dep] += 1
            incoming[arr] += 1
        for i in range(1,n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1