# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tsk = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tsk.sort()

        res = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            while i < n and tsk[i][0] <= time:
                heapq.heappush(heap, (tsk[i][1], tsk[i][2]))
                i += 1
            
            if heap:
                proc, idx = heapq.heappop(heap)
                time += proc
                res.append(idx)
            else:
                if i < n:
                    time = tsk[i][0]

        return res
