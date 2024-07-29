# Problem: B - Chef Jamie - https://codeforces.com/gym/537575/problem/B

n = int(input())
fruits = list(map(int,input().split()))
sorted_fruits = sorted(fruits)
res = 0

for i in range(n):
    if sorted_fruits[i] != fruits[i]:
        res += 1
print(res-1) if res > 0 else print(0)