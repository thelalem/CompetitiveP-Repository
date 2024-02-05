if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lists = []
    for i in arr:
        lists.append(i)
    lists.sort(reverse= True)
    for i in lists:
        if i < lists[0]:
            print(i)
            break
