# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-freq,letter) for letter, freq in counter.items()]
        heapq.heapify(max_heap)

        prev_char = ''
        prev_freq = 0
        res = []


        while max_heap:
            freq,char = heapq.heappop(max_heap)
            res.append(char)
            if prev_freq < 0:
                heapq.heappush(max_heap,(prev_freq,prev_char))
            prev_char = char
            prev_freq = freq + 1
            
        if len(res) == len(s):
            return("".join(res))
        else:
            return("")