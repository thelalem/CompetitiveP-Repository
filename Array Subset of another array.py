from collections import Counter

def isSubset(a1, a2, n, m):
    count_a1 = Counter(a1)
    count_a2 = Counter(a2)
    
    for num, count in count_a2.items():
        if count_a1[num] < count:
            return "No"
    
    return "Yes"
