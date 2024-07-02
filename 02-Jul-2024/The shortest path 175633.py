# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque

def short(n, m, a, b, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([a])
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    
    visited[a] = True

    while queue:
        current = queue.popleft()
        if current == b:
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    
    if not visited[b]:
        return -1, []
    
    path = []
    current = b
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    return len(path) - 1, path
n, m = map(int, input().split())
a, b = map(int, input().split())
edges = [(map(int, input().split())) for _ in range(m)]
l, path = short(n, m, a, b, edges)
if l == -1:
    print(l)
else:
    print(l)
    print(" ".join(map(str, path)))
