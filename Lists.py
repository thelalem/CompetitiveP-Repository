if __name__ == '__main__':
    N = int(input())
    mylist = []

    for i in range(N):
        command = input().split()

        if command[0] == "insert":
            mylist.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(mylist)
        elif command[0] == "remove":
            e = int(command[1])
            mylist.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            mylist.append(e)
        elif command[0] == "sort":
            mylist.sort()
        elif command[0] == "pop":
            mylist.pop()
        elif command[0] == "reverse":
            mylist.reverse()
