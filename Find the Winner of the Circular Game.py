class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lists = list(range(1,n + 1))
        
        i = 0
        while len(lists) > 1:
            i = (i+k -1) % len(lists)
            lists.pop(i)
        return lists[0]
