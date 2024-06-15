# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict

n = int(input())

k = int(input())

graph = defaultdict(list)

for _ in range(k):
    operation = input().split()
    oprtype = int(operation[0])
    
    if oprtype == 1:
        u,v = map(int, operation[1:])
        graph[u].append(v)
        graph[v].append(u)
    else:
        u = int(operation[1])
        if graph[u]:
            print(" ".join(map(str, sorted(graph[u]))))
        else:
            print("")
