# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        ancestors = [set() for _ in range(n)]
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            node = queue.popleft()
            for child in adj_list[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
                    
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]
