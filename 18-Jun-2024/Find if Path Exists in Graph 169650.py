# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    found = dfs(neigh)
                    if found:
                        return True
            return False
        visited = set()
        return dfs(source)