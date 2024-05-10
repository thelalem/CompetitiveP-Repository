# Problem:  a-Good String - https://codeforces.com/gym/522997/problem/C

def solve(s, c):
    if len(s) == 1:
        if s[0] == c:
            return 0
        else:
            return 1

    one = 0
    two = 0
    n = len(s)
    for i in range(n):
        if i < n // 2:
            if s[i] == c:
                one += 1
        else:
            if s[i] == c:
                two += 1
    c = chr(ord(c) + 1)
    left = solve(s[:n // 2], c)
    right = solve(s[n // 2:], c)

    return min((n // 2) - one + right, (n // 2) - two + left)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(solve(s, 'a'))
