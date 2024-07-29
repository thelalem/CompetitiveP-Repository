# Problem: C - Experiment - https://codeforces.com/gym/537575/problem/C

n = int(input())
max_size = int(1e4+10)
ps = [0] * max_size

experiments = []
for _ in range(n):
    si, ti, bi = map(int, input().strip().split())
    experiments.append((si, ti, bi))
for experiment in experiments:
    s, t, b = experiment
    ps[s] += b
    ps[t + 1] -= b

result = 0
current_rooms = 0

for i in range(1, max_size):
    current_rooms += ps[i]
    result = max(result, current_rooms)

print( result)