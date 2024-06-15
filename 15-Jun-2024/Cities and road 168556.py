# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

road_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] == 1:
            road_count += 1
print(road_count)