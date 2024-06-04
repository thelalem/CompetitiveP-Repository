# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtracking(index,prev):
            if index == len(s):
                return True
            for j in range(index,len(s)):
                val = int(s[index:j +1])
                if val + 1 == prev and backtracking(j+1,val):
                    return True
            return False

        for i in range(len(s) - 1):
            val = int(s[:i+1])
            if backtracking(i+1,val):
                return True
        return False