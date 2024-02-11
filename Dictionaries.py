import sys
n = int(input())
phonebook = {}
for _ in range(n):
    name, phone = map(str, input().split())
    phonebook[name] = phone
while True:
    query = sys.stdin.readline().strip()
    if not query:
        break
    if query in phonebook:
        print(query + "=" + phonebook[query])
    else:
        print("Not found")
