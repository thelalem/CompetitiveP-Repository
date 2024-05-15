# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    max_team = min((a+b)//4, min(a,b))
    print(max_team)