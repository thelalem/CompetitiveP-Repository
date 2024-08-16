# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

def dfs(v, visited, parent):
        visited[v] = True
        
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if dfs(neighbour, visited, v):
                    return True
            elif neighbour != parent:
                return True
                
        return False

    visited = [False] * V
    
    for i in range(V):
        if not visited[i]:
            if dfs(i, visited, -1):
                return 1

    return 0  