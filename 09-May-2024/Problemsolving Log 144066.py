# Problem: Problemsolving Log - https://codeforces.com/gym/522997/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    log = input()
    time_required = [0]*26
    solved = 0
    
    for i in range(n):
        time_required[ord(log[i]) - ord('A')] += 1
        if time_required[ord(log[i]) - ord('A')] == (ord(log[i]) - ord('A') + 1):
            solved += 1
    print(solved)