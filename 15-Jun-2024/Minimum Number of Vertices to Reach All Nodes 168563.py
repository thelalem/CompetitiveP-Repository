# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(list)

        for dep,arr in edges:
            incoming[arr].append(dep)
        res = []
        for i in range(n):
            if not incoming[i]:
                res.append(i)
        return res
