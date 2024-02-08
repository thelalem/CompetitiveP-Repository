class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = 0
        temp_max = 0
        for num in nums:
            if num == 1:
                temp_max +=1
            else:
                if temp_max > maximum:
                    maximum = temp_max
                temp_max = 0
        return max(maximum,temp_max)