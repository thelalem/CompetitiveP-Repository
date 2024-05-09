# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def find_twos(num):
    count = 0
    while num %2 == 0:
        num//=2
        count += 1
    return count
t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    nums = list(map(int, input().split()))
    for num in nums:
        total += find_twos(num)
    twos_indexes = []
    for i in range(1,n+1):
        count = find_twos(i)
        twos_indexes.append(count)
    twos_indexes.sort(reverse=True)
    i = 0
    ops = 0
    while total < n and i < len(twos_indexes):
        total += twos_indexes[i]
        i += 1
        ops += 1
    print(ops) if total >= n else print(-1) 