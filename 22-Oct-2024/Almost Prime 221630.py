# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
prime_factors = [0] * (n + 1)
for i in range(2, n + 1):
    if prime_factors[i] == 0:  
        for j in range(i, n + 1, i):
            prime_factors[j] += 1

count = 0
for i in range(1, n + 1):
    if prime_factors[i] == 2:
        count += 1

print( count)