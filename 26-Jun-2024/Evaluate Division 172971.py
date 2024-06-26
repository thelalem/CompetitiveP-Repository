# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,eq in enumerate(equations):
            a,b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a,1/values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q,visit = deque(),set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n,w = q.popleft()
                if n == target:
                    return w
                for neigh, weigh in adj[n]:
                    if neigh not in visit:
                        q.append([neigh,w*weigh])
                        visit.add(neigh)
                    
            return -1



        return [bfs(q[0],q[1]) for q in queries]
