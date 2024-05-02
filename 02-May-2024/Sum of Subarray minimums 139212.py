# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = []

        for i,n in enumerate(arr):
            while stack and n < stack[-1][1]:
                idx,val = stack.pop()
                left = idx - stack[-1][0] if stack else idx+1
                right = i - idx
                res = (res+val * left * right) % MOD
            stack.append((i,n))
        
        for i in range(len(stack)):
            j,val = stack[i]
            left = j - stack[i - 1][0] if i > 0 else j+1
            right = len(arr) - j
            res = ((res+val * left * right) % MOD)

        return res