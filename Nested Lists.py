if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    records.sort(key = lambda x: x[1])
    for i in range(len(records)):
        if records[i][1] > records[0][1]:
            second_lowest = records[i][1]
            break
    names = sorted([name for name,score in records if score == second_lowest])
    for name in names:
        print(name)
