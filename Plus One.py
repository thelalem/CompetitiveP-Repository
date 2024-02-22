class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(str(d) for d in digits)
        num = int(num) + 1
        num = str(num)
        return [int(digit) for digit in num]
