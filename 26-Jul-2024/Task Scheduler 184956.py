# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dc = Counter(tasks)
        maxHeap = [-count for count in dc.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if maxHeap:
                count = 1+heapq.heappop(maxHeap)
                if count:
                    q.append([count,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time