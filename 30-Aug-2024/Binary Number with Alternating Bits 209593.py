# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shift = n >> 1
        XOR = n^shift

        return (XOR & (XOR+1)) == 0