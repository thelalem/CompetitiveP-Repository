class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dc = {}
        lists = []
        min_val = 9999
        for i,n in enumerate(list1):
            dc[n] = i
        for i,n in enumerate(list2):
            if n in dc:
                min_index = i + dc[n]
                if min_index < min_val:
                    min_val =  min_index
                    lists = [n]
                elif min_index == min_val:
                    lists.append(n)
        return lists