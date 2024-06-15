# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Convert the adjacency matrix to adjacency list
adjacency_list = []
for i in range(n):
    current_list = []
    for j in range(n):
        if matrix[i][j] == 1:
            current_list.append(j + 1) 
    adjacency_list.append(current_list)
for neighbors in adjacency_list:
    print(len(neighbors), ' '.join(map(str, neighbors)))
