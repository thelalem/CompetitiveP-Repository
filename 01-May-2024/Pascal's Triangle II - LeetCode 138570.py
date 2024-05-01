# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for k in range(1, rowIndex+1):
            val = row[k-1] * (rowIndex - k +1)//k
            row.append(val)
        return row