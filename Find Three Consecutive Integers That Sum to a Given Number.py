class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 == 0:
            nums = num//3
            return [nums-1,nums,nums+1]
        else:
            return []