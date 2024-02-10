k = int(input())
max = 0
passenger = 0
for _ in range(k):
    exit,enter = map(int,input().split())
    passenger -= exit
    passenger += enter
    if passenger > max:
        max = passenger
print(max)
