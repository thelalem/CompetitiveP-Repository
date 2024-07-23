# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        idx = 0
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        for i in range(len(gas)):
            total += diff[i]
            if total < 0:
                total = 0
                idx = i +1
        return idx