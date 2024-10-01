# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            twos |= ones & num

            ones ^= num

            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        
        return ones