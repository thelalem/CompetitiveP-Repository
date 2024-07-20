# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

n, m, a = map(int, input().split())
length = (n + a - 1) // a
width = (m + a - 1) // a
total = length * width
print(total)
