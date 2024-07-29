# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

s = input()
stack = []
res = 0
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
            res += 2
print(res)