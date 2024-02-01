def swap_case(s):
    t = ""
    for i in s:
        if i.isupper():
            t += i.lower()
        else:
            t += i.upper()
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
