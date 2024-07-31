# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        for src in range(n):
            for dst in graph[src]:
                reverse_graph[dst].append(src)
            out_degree[src] = len(graph[src])
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe_nodes = []
        
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        safe_nodes.sort()
        return safe_nodes