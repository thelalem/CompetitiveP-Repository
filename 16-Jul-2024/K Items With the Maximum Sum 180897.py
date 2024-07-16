# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        for i in range(k):
            if numOnes > 0:
                res += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            else:
                res -= 1
                numNegOnes -= 1
        return res
