# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dc = {char:i for i,char in enumerate(s)}
        res = []
        start = 0
        end = 0
        for i,char in enumerate(s):
            end = max(end,dc[char])
            if i == end:
                res.append(end-start+1)
                start = end+1
        return res