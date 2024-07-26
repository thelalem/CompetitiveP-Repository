# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dc = Counter(tasks)
        max_count = max(dc.values())
        max_task = 0
        for i in dc:
            if dc[i] == max_count:
                max_task += 1
        result = max((max_count - 1) * (n + 1) + max_task, len(tasks))

        return result