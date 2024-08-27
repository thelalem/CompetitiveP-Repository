# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        lists = []
        for i in range(n+1):
            lists.append(bin(i).count('1'))
        return lists
