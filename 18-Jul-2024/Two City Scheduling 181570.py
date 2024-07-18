# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for a,b in costs:
            diff.append([b - a,a,b])
        diff.sort()
        res = 0
        for i in range(len(diff)):
            if i < len(diff)//2:
                res += diff[i][2]
            else:
                res += diff[i][1]
        return res